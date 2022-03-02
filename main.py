from src import IO, preprocessing, burst_calc, plot_utils, postprocessing
import numpy as np
import pandas as pd
import csv
from scipy.stats import wilcoxon


def main():
    # 1. READ IN DATA #
    PATH_BIDS = r'/Users/alidzaye/rawdata'
    PATH_RUN = r'/Users/alidzaye/rawdata/sub-003/ses-EphysMedOff01/ieeg/sub-003_ses-EphysMedOff01_task-Rest_acq-StimOff_run-01_ieeg.vhdr'

    #raw_on = IO.get_runs(PATH_BIDS, med_on = True)
    #raw_off = IO.get_runs(PATH_BIDS, med_on = False)
    # data, sfreq, line_freq 

    raw, data, sfreq, line_freq = IO.read_BIDS_data(PATH_RUN, PATH_BIDS)

    new_ch_names = ['ECOG_L1_L2_SMC',
               'ECOG_L2_L3_SMC',
               'ECOG_L3_L4_SMC',
               'ECOG_L4_L5_SMC',
              'ECOG_L5_L6_SMC']
    
    #NUM_CH = data.shape[0] # might be 1

    m1 = 3

    raw_ecog = preprocessing.pick_ecog(raw)

    #raw_ecog_red = raw_ecog

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
    power_spectra_norm = [p_ch/np.sum(p_ch[4:45] + np.sum(p_ch[54:95])) for p_ch in power_spectra]

    # Burst duration 
    burst_duration = [burst_calc.get_burst_length(l, l_beta_thr[2][idx], sfreq=250) for idx, l in enumerate(l_beta_avg_norm[2])] 
    burst_duration_m1_cl = [ i for i in burst_duration[m1] if i >= 0.1]

    # Histogram of burst duration up to 10 sec
    histogram_duration = [np.histogram(burst_duration[ch_idx], density=False, bins=20, range=(0, 2))[0] for ch_idx in range(NUM_CH)] 
    histogram_duration_m1_cl = [np.histogram(burst_duration_m1_cl, density=False, bins=20, range=(0, 2))] 
    hist_dur_m1 = histogram_duration_m1_cl[0][0]

    # Normed Histogram
    norm_histogram_duration = [100 * histogram_duration[ch_idx] / burst_duration[ch_idx].shape[0] for ch_idx in range(NUM_CH)]
    norm_histogram_duration_m1 = [100 * hist_dur_m1 / len(burst_duration_m1_cl)]
    norm_hist_m1 = norm_histogram_duration_m1[0]

    # Mean burst duration in channels 
    mean_burst_duration = [np.nanmean(burst_duration[ch_idx], axis=0) for ch_idx in range(NUM_CH)]
    mean_dur_m1 = np.nanmean(burst_duration_m1_cl, axis=0)

    # Histogram Duration M1
    #histogram_M1 = norm_histogram_duration[m1]

    # Burst Amplitude M1
    bursts_amplitude = burst_calc.get_mean_burst_amplitude(l_beta_avg_norm[2][m1], l_beta_thr[2][m1])



    #bursts = [ i for i in l_beta_avg_norm[2][m1] > l_beta_thr[2][m1]] 
    #burst_amplitude_M1 = np.nanmean(bursts)

    # Burst Rate M1
    burst_rate_M1 = np.sum(histogram_duration[m1]) / raw.times[-1]

    # PSD M1
    psd_M1 = power_spectra_norm[m1]


    # 3. STRUCTURE FEATURES IN PANDAS AND SAVE EXCEL FILES #

    #burst_char_pd = postprocessing.dataframe_burst_char(mean_burst_duration_M1,burst_amplitude_M1,burst_rate_M1, histogram_M1)
    #burst_char_pd.to_excel('burst_char_S7_On4.xlsx')

    # M1 Mean Burst Duration 
    #M1_mean_burst_duration = postprocessing.dataframe_mean_duration_m1(mean_burst_duration_M1)
    #np.savetxt('M1_mean_burst_duration_S7_On1.csv', mean_burst_duration)
    #M1_mean_burst_duration.to_excel('M1_mean_burst_duration_S4_On5.xlsx')

    # normalized beta power
    npow = postprocessing.dataframe_npow(power_spectra_norm)
    npow.to_excel('nPSD_S7_On1.xlsx')

    # M1 Beta Burst Dynamics 
    #M1_burst_dynamics = postprocessing.dataframe_burst_dynamics(norm_histogram_duration[4])
    #M1_burst_dynamics.to_excel('Histogram_S7_On4.xlsx')
   
    # Beta Burst Duration
    #burst_duration = postprocessing.dataframe_burst_duration(burst_duration)
    #burst_duration.to_csv('mean_duration.csv')

    
    # M1 Beta Burst Length 
    #M1_burst_duration = postprocessing.dataframe_burst_duration(burst_duration[4])


    # 4. STATISTICAL COMPARISON WITH WILCOXON TEST #
    #w, p = wilcoxon(M1_mean_burst_duration) #ON

if __name__ == "__main__":
    main()