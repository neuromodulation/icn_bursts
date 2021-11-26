from src import IO, burst_calc, plot_utils, preprocessing, burst_calc
import numpy as np
import pandas as pd


def main():
    
    PATH_BIDS = r'/Users/alidzaye/rawdata'
    PATH_RUN = r'/Users/alidzaye/rawdata/sub-003/ses-EphysMedOff01/ieeg/sub-003_ses-EphysMedOff01_task-Rest_acq-StimOff_run-01_ieeg.vhdr'
    
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

    l_beta = burst_calc.beta_bands(run_TF)  # contains list of low, high, full beta lists

    ## Averaging power in all beta bands 
    l_beta_avg = [burst_calc.avg_power(l) for l in l_beta]

    ## Z-Scored averaged beta traces
    l_beta_avg_norm = [burst_calc.zscore(l) for l in l_beta_avg]

    ## 75th percentile of the power
    l_beta_thr = [burst_calc.percentile(l, percentile=75) for l in l_beta_avg_norm]

    # 2.CALCULATING FEATURES (NORMALIZED POWER, BURST LENGTH, BURST DYNAMIC) AND BIOMARKER COMPARISON #
    power_spectra = [np.nanmean(np.squeeze(run_TF[ch_idx, :, :]), axis=0) for ch_idx in range(NUM_CH)]

    ## Normalized power spectral density (statistical comparison)
    power_spectra_norm = [p_ch/np.sum(p_ch[4:45] + np.sum(p_ch[54:95])) for p_ch in power_spectra]

    ## M1 normalized beta power OFF vs ON (Pandas)
    pw = pd.DataFrame(power_spectra_norm[4])

    pw_on = pd.DataFrame(power_spectra_norm[4]) # Why shoudl that be on?

    pw_a = pw.assign(Location='ECOG-L4-L5_SMC_AT', Medication = 'OFF')
    pw_on_a = pw_on.assign(Location='ECOG-L4-L5_SMC_AT', Medication = 'ON')

    pw_r = pw_a.rename(columns={0:'Relative spectral power (au)'}) 
    pw_r_on = pw_on_a.rename(columns={0:'Relative spectral power (au)'}) 

    pw_c = pd.concat([pw_r, pw_r_on])

    # burst length
    burst_duration = [burst_calc.get_burst_length(l_beta_avg_norm, l_beta_thr, sfreq=250) for l in l_beta_avg_norm] 




    
if __name__ == "main":
    main()