import mne
from mne_bids import BIDSPath, read_raw_bids, print_dir_tree, make_report
import numpy as np
import os
from os.path import join
from bids import BIDSLayout

# Initialize the layout
data_path = os.path.join('/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata')

layout = BIDSLayout(data_path)

subjects = layout.get_subjects()

sessions = layout.get_session()

tasks = layout.get_tasks()

stimulation = layout.get_acquisition()

# get Rest Data ON & OFF all subjects
files = layout.get(extension='vhdr', task='Rest',acquisition='StimOff', return_type='filename')
files_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff', session=['EcogLfpMedOn01', 'EcogLfpMedOn01', 'EcogLfpMedOn01'],return_type='filename')

# get Rest Data ON & OFF all subjects
files1 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='001', return_type='filename')
files1_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='001', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files1_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='001', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files3 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='003', return_type='filename')
files3_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='003', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files3_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='003', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files4 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='004', return_type='filename')
files4_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='004', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files4_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='004', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files5 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='005', return_type='filename')
files5_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='005', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files5_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='005', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files6 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='006', return_type='filename')
files6_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='006', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files6_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='006', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files7 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='007', return_type='filename')
files7_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='007', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files7_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='007', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files8 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='008', return_type='filename')
files8_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='008', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files8_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='008', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files9 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='009', return_type='filename')
files9_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='009', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files9_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='009', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

files10 = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='010', return_type='filename')
files10_off = layout.get(extension='vhdr', task='Rest',acquisition='StimOff',subject='010', session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'], return_type='filename')
files10_on = layout.get(extension='vhdr', task='Rest', acquisition='StimOff',subject='010', session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],return_type='filename')

# M1 and Runs in all subjects
#1
# M1 = 2
# OFF = 2
# ON = 2

#3
# M1 = 3
# OFF = 3
# ON = 2

#4
# M1 = 4
# OFF = 2
# ON = 5

#5
# M1 = 4
# OFF = 3
# ON = 2

#6
# M1 = 2
# OFF = 2
# ON = 2

#7
# M1 = 3 (4-5)
# OFF = 1
# ON = 4

#8
# M1 = 4
# OFF = 1
# ON = 2

#9
# M1 = 2
# OFF = 4
# ON = 1

#10
# M1 = 4
# OFF = 1
# ON = 1


from src import IO, preprocessing, burst_calc, plot_utils, postprocessing
import numpy as np
import pandas as pd


def main():
    # 1. READ IN DATA #
    PATH_BIDS = r'/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata'
    PATH_RUN = files3[0]

    raw, data, sfreq, line_freq = IO.read_BIDS_data(PATH_RUN, PATH_BIDS)


    raw_ecog = preprocessing.pick_ecog(raw)

    new_ch_names = ['ECOG_L_1_2_SMC_AT',
               'ECOG_L_2_3_SMC_AT',
               'ECOG_L_3_4_SMC_AT',
               'ECOG_L_4_5_SMC_AT',
               'ECOG_L_5_6_SMC_AT']

    m1 = 3

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


    # 2. CALCULATING FEATURES (NORMALIZED POWER, BURST LENGTH, BURST DYNAMIC) AND BIOMARKER COMPARISON #
    # Power spectral density
    power_spectra = [np.nanmean(np.squeeze(run_TF[ch_idx, :, :]), axis=1) for ch_idx in range(len(raw_ecog_bi.get_channel_types()))]

    # Normalized power spectral density (statistical comparison)
    power_spectra_norm = [p_ch/np.sum(p_ch[4:45] + p_ch[54:95]) for p_ch in power_spectra]

    # Burst duration 
    burst_duration = [burst_calc.get_burst_length(l, l_beta_thr[2][idx], sfreq=250) for idx, l in enumerate(l_beta_avg_norm[2])] 
    burst_duration_m1_cl = [ i for i in burst_duration[m1] if i >= 0.1]

    # Histogram of burst duration up to
    histogram_duration = [np.histogram(burst_duration[ch_idx], density=False, bins=20, range=(0, 2))[0] for ch_idx in range(NUM_CH)] 
    histogram_duration_m1_cl = [np.histogram(burst_duration_m1_cl, density=False, bins=20, range=(0, 2))] 
    hist_dur_m1 = histogram_duration_m1_cl[0][0]

    # Normed Histogram
    norm_histogram_duration = [100 * histogram_duration[ch_idx] / burst_duration[ch_idx].shape[0] for ch_idx in range(NUM_CH)]
    norm_histogram_duration_m1 = [100 * hist_dur_m1 / len(burst_duration_m1_cl)]
    norm_hist_m1 = norm_histogram_duration_m1[0]
    norm_hist_m1_cl = np.delete(norm_hist_m1,0)
    short_bursts = norm_hist_m1_cl[:7]
    prol_bursts = np.sum(norm_hist_m1_cl[7:])
    nhist_m1 = np.append(short_bursts, prol_bursts)


    # Mean burst duration in channels 
    mean_burst_duration = [np.nanmean(burst_duration[ch_idx], axis=0) for ch_idx in range(NUM_CH)]
    mean_dur_m1 = np.nanmean(burst_duration_m1_cl, axis=0)

    # Burst Amplitude M1
    bursts_amplitude = burst_calc.get_mean_burst_amplitude(l_beta_avg_norm[2][m1], l_beta_thr[2][m1])

    # Burst Rate M1
    burst_rate_M1 = np.sum(hist_dur_m1 / raw.times[-1])

    # PSD M1
    psd_M1 = power_spectra_norm[m1]


    # 3. STRUCTURE AND SAVE FEATURES #

    burst_char_pd = postprocessing.dataframe_burst_char(mean_dur_m1, bursts_amplitude, burst_rate_M1)
    
    # M1 Beta Burst Dynamics 
    M1_burst_dynamics = postprocessing.dataframe_burst_dynamics(nhist_m1)
    

    # normalized beta power
    npow = postprocessing.dataframe_npow(psd_M1)
    
    M1_burst_dynamics
    mean_dur_m1


    with pd.ExcelWriter('sub10_On_r1.xlsx') as writer:  
        burst_char_pd.to_excel(writer, sheet_name="Features")
        M1_burst_dynamics.to_excel(writer, sheet_name="Dynamics")
        npow.to_excel(writer, sheet_name="PSD")


if __name__ == "__main__":
    main()

