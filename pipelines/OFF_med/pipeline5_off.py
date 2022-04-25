import mne
from mne_bids import BIDSPath
import numpy as np
import pandas as pd
import os
from os.path import join
from bids import BIDSLayout
from src import IO, preprocessing, burst_calc, plot_utils, postprocessing

# Initialize the layout 
data_path = os.path.join('/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata')
layout = BIDSLayout(data_path)

files5 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='005', return_type='filename')
files5_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='005', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files5_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='005', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

# 3 runs

# SCRIPT START #

def main():
    # 1. READ BIDS RECORDING #
    PATH_BIDS = r'/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata'
    PATH_RUN = files5_off[2]
    raw, data, sfreq, line_freq = IO.read_BIDS_data(PATH_RUN, PATH_BIDS)
    raw_ecog = preprocessing.pick_ecog(raw)
    new_ch_names = ['ECOG_L_1_2_SMC_AT',
               'ECOG_L_2_3_SMC_AT',
               'ECOG_L_3_4_SMC_AT',
               'ECOG_L_4_5_SMC_AT',
               'ECOG_L_5_6_SMC_AT']
    m1 = 4
    raw_ecog_bi = preprocessing.bipolar_reference(raw, raw_ecog, new_ch_names)

    NUM_CH = len(raw_ecog_bi.get_channel_types())

    raw_ecog_filt = preprocessing.filtering(raw_ecog_bi)

    raw_ecog_dow = preprocessing.downsample(raw_ecog_filt)

    signal = preprocessing.get_data(raw_ecog_dow)

    stand_signal = preprocessing.z_score_signal(signal)

    run_TF = burst_calc.Time_Frequency_Estimation(stand_signal)

    # list of low, high, full beta bands for all channels
    l_beta = burst_calc.beta_bands(run_TF) 

    # Averaging power in all beta bands 
    l_beta_avg = [burst_calc.avg_power(l) for l in l_beta]

    # Z-Scored averaged beta traces
    l_beta_avg_norm = [burst_calc.z_score(l) for l in l_beta_avg]

    # 75th percentile of the power
    l_beta_thr = [burst_calc.percentile(l, percentile=75) for l in l_beta_avg_norm]

    low = 0
    high = 1 
    full = 2

    # 2. CALCULATING FEATURES (NORMALIZED POWER, BURST LENGTH, BURST DYNAMIC) AND BIOMARKER COMPARISON #
    # Power spectral density
    power_spectra = [np.nanmean(np.squeeze(run_TF[ch_idx, :, :]), axis=1) for ch_idx in range(len(raw_ecog_bi.get_channel_types()))]
    # Normalized power spectral density 
    power_spectra_norm = [p_ch/np.sum(p_ch[4:45] + p_ch[54:95]) for p_ch in power_spectra]
    psd_M1 = power_spectra_norm[m1]

    # Burst duration 
    burst_duration = [burst_calc.get_burst_length(l, l_beta_thr[full][idx], sfreq=200) for idx, l in enumerate(l_beta_avg_norm[full])] 
    burst_duration_cl = [burst_calc.exclude_short_bursts (burst_duration[ch_idx]) for ch_idx in range(NUM_CH)]
    burst_duration_cl_m1 = burst_duration_cl[m1]
    # Mean burst duration 
    mean_burst_duration = [np.nanmean(burst_duration_cl[ch_idx], axis=0) for ch_idx in range(NUM_CH)]
    mean_dur_m1 = mean_burst_duration[m1]

    # Histogram of burst duration 
    histogram_duration = [np.histogram(burst_duration_cl[ch_idx], density=False, bins=20, range=(0, 2))[0] for ch_idx in range(NUM_CH)] 
    hist_dur_m1 = histogram_duration[m1]
    # Normed Histogram
    n_hist_dur = [100 * histogram_duration[ch_idx] / len(burst_duration_cl[ch_idx]) for ch_idx in range(NUM_CH)]
    n_hist_dur_m1 = n_hist_dur[m1]
    n_hist_dur_m1_cl = np.delete(n_hist_dur_m1,0)
    short_bursts = n_hist_dur_m1_cl[:7]
    prol_bursts = np.sum(n_hist_dur_m1_cl[7:])
    normhist_dur_m1 = np.append(short_bursts, prol_bursts)

    # Burst Amplitude 
    burst_amplitude = [burst_calc.get_mean_burst_amplitude(l,l_beta_thr[full][idx]) for idx,l in enumerate(l_beta_avg_norm[full])]
    burst_amplitude_m1 = burst_amplitude[m1]

    # Burst Rate 
    burst_rate = [np.sum(histogram_duration[ch_idx] / raw.times[-1])for ch_idx in range(len(raw_ecog_bi.get_channel_types()))]
    burst_rate_m1 = burst_rate[m1] 

    # 3. STRUCTURE AND SAVE FEATURES #
    # Burst Features
    burst_char_pd = postprocessing.dataframe_burst_char(mean_dur_m1, burst_amplitude_m1, burst_rate_m1)
    
    # M1 Beta Burst Dynamics 
    M1_burst_dynamics = postprocessing.dataframe_burst_dynamics(normhist_dur_m1)

    # normalized beta power
    npow = postprocessing.dataframe_npow(psd_M1)
    

    with pd.ExcelWriter('sub5_Off_r3.xlsx') as writer:  
        burst_char_pd.to_excel(writer, sheet_name="Features")
        M1_burst_dynamics.to_excel(writer, sheet_name="Dynamics")
        npow.to_excel(writer, sheet_name="PSD")


if __name__ == "__main__":
    main()

