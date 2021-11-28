from src import IO, burst_calc, plot_utils, preprocessing, burst_calc, saving_feat
import numpy as np
import pandas as pd
import csv
from scipy.stats import wilcoxon


def main():
    # 1. READ IN DATA #

    PATH_BIDS = r'/Users/alidzaye/rawdata'
    PATH_RUN = r'/Users/alidzaye/rawdata/sub-003/ses-EphysMedOff01/ieeg/sub-003_ses-EphysMedOff01_task-Rest_acq-StimOff_run-01_ieeg.vhdr'

    raw_on = IO.get_runs(PATH_BIDS, med_on = True)
    raw_off = IO.get_runs(PATH_BIDS, med_on = False)
    
    raw, dat, sfreq, line_freq = IO.read_BIDS_data(PATH_RUN, PATH_BIDS)

    new_ch_names = ['ECOG_L_1_SMC_BI',
               'ECOG_L_2_SMC_BI',
               'ECOG_L_3_SMC_BI',
               'ECOG_L_4_SMC_BI',
              'ECOG_L_5_SMC_BI']
    
    NUM_CH = dat.shape[0] # might be 1

    raw_ecog = preprocessing.pick_ecog(raw)

    raw_ecog_bi = preprocessing.bipolar_reference(raw_ecog)

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
    l_beta_avg_norm = [burst_calc.zscore(l) for l in l_beta_avg]

    # 75th percentile of the power
    l_beta_thr = [burst_calc.percentile(l, percentile=75) for l in l_beta_avg_norm]


    # 2. CALCULATING FEATURES (NORMALIZED POWER, BURST LENGTH, BURST DYNAMIC) AND BIOMARKER COMPARISON #
    # Power spectral density
    power_spectra = [np.nanmean(np.squeeze(run_TF[ch_idx, :, :]), axis=0) for ch_idx in range(NUM_CH)]

    # Normalized power spectral density (statistical comparison)
    power_spectra_norm = [p_ch/np.sum(p_ch[4:45] + np.sum(p_ch[54:95])) for p_ch in power_spectra]

    # Burst duration 
    burst_duration = [burst_calc.get_burst_length(l_beta_avg_norm, l_beta_thr, sfreq=250) for l in l_beta_avg_norm] 

    # Histogram of burst duration up to 10 sec
    histogram_duration = [np.histogram(burst_duration, density=False, bins=100, range=(0, 10)) for ch_idx in range(NUM_CH)] 

    # Normed Histogram
    norm_histogram_duration = [100 * histogram_duration / burst_duration.shape[0] for ch_idx in range(NUM_CH)]

    # Mean burst duration in channels 
    mean_burst_duration = [np.nanmean(burst_duration, axis=0) for ch_idx in range(NUM_CH)]

    # M1 Mean burst duration
    M1_mean_burst_duration = mean_burst_duration[4]


    # 3. SAVING FEATURES IN PANDAS AND CSV FILES #
    # Save (M1) Mean Burst Duration in csv
    mean_duration = saving_feat.save_mean_duration(mean_burst_duration)
    M1_mean_duration = saving_feat.save_mean_duration(M1_mean_burst_duration)
    mean_duration.to_csv('mean_burst_duration_run_.csv')
   
    # Beta Burst Duration (Pandas)
    burst_duration = saving_feat.save_burst_duration(burst_duration)

    # M1 normalized beta power OFF vs ON (Pandas)
    M1_npow = saving_feat.save_npow(power_spectra_norm[4])

    # M1 Beta Burst Dynamics (Pandas)
    M1_burst_dynamics = saving_feat.save_burst_dynamics(norm_histogram_duration[4])
    
    # M1 Beta Burst Length (Pandas)
    M1_burst_duration = saving_feat.save_burst_duration(burst_duration[4])


    # 4. STATISTICAL COMPARISON WITH WILCOXON TEST #
    w, p = wilcoxon(M1_mean_burst_duration) #ON
    
if __name__ == "main":
    main()