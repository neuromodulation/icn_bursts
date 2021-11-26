#import libraries and modules
from operator import index
import mne
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as  pd
import mne_bids
import string
import os
from os.path import join
from bids import BIDSLayout
import csv





##Artefact Detection
# plot filtered ecog channels for annotiations
# %matplotlib qt
# raw_ecog_filt.plot(scalings='auto', highpass=3, lowpass=95, decim='auto')
# raw_ecog_filt.annotations.save('run.txt', overwrite=True)






















# 2.CALCULATING FEATURES (NORMALIZED POWER, BURST LENGTH, BURST DYNAMIC) AND BIOMARKER COMPARISON #

## Normalized power spectral density (statistical comparison)
power_spectrum_for_channel_1 = np.nanmean(np.squeeze(run_TF[0,:,:]), axis=1)
power_spectrum_for_channel_2 = np.nanmean(np.squeeze(run_TF[1,:,:]), axis=1)
power_spectrum_for_channel_3 = np.nanmean(np.squeeze(run_TF[2,:,:]), axis=1)
power_spectrum_for_channel_4 = np.nanmean(np.squeeze(run_TF[3,:,:]), axis=1)
power_spectrum_for_channel_5 = np.nanmean(np.squeeze(run_TF[4,:,:]), axis=1)

npow_1 = power_spectrum_for_channel_1/np.sum(power_spectrum_for_channel_1[4:45] + power_spectrum_for_channel_1[54:95])
npow_2 = power_spectrum_for_channel_2/np.sum(power_spectrum_for_channel_2[4:45] + power_spectrum_for_channel_2[54:95])
npow_3 = power_spectrum_for_channel_3/np.sum(power_spectrum_for_channel_3[4:45] + power_spectrum_for_channel_3[54:95])
npow_4 = power_spectrum_for_channel_4/np.sum(power_spectrum_for_channel_4[4:45] + power_spectrum_for_channel_4[54:95])
npow_5 = power_spectrum_for_channel_5/np.sum(power_spectrum_for_channel_5[4:45] + power_spectrum_for_channel_5[54:95])

## M1 normalized beta power OFF vs ON (Pandas)
pw = pd.DataFrame(npow_4)
pw_on = pd.DataFrame(npow_4_on)

pw_a = pw.assign(Location='ECOG-L4-L5_SMC_AT', Medication = 'OFF')
pw_on_a = pw_on.assign(Location='ECOG-L4-L5_SMC_AT', Medication = 'ON')

pw_r = pw_a.rename(columns={0:'Relative spectral power (au)'}) 
pw_r_on = pw_on_a.rename(columns={0:'Relative spectral power (au)'}) 

pw_c = pd.concat([pw_r, pw_r_on])
#pw_c.to_csv('M1_Relative_Power.csv')

# Characterization of beta bursts
## Analysing the duration of beta burst 
def get_burst_length(beta_averp_norm,beta_thr, sfreq=250):
    """
    Burst Duration
    """
    deriv = np.diff (beta_averp_norm >= beta_thr) 
    isburst = False
    burst_length = []
    burst_start = 0

    for index, i in enumerate(deriv):
        if i == True:
            if isburst == True:
                burst_length.append(index - burst_start)

                isburst = False
            else:
                burst_start = index
                isburst = True
    burst_length = np.array(burst_length)/sfreq
    
    return burst_length

## Burst durration of full beta
burst_length_1 = get_burst_length(full_beta_1_averp_norm,full_beta_1_thr, sfreq = 250)
burst_length_2 = get_burst_length(full_beta_2_averp_norm,full_beta_2_thr, sfreq = 250)
burst_length_3 = get_burst_length(full_beta_3_averp_norm,full_beta_3_thr, sfreq = 250)
burst_length_4 = get_burst_length(full_beta_4_averp_norm,full_beta_4_thr, sfreq = 250)
burst_length_5 = get_burst_length(full_beta_5_averp_norm,full_beta_5_thr, sfreq = 250)

## Burst duration in all channels ON vs OFF (Pandas)
burst_duration_allCh = [burst_length_1,burst_length_2,burst_length_3,burst_length_4,burst_length_5]
burst_duration_allCh_on = [burst_length_1_on,burst_length_2_on,burst_length_3_on,burst_length_4_on,burst_length_5_on]

df_dur = pd.DataFrame(burst_duration_allCh)
df_dur_on = pd.DataFrame(burst_duration_allCh_on) 

df_dur_t=df_dur.T
df_dur_t_on=df_dur_on.T

df_dur_t_r = df_dur_t.rename(columns={0: "secondary somatosensory cortex",1: "secondary/primary somatosensory cortex",2:'primary somatosensory cortex',3:'primary motor cortex',4:'premotor cortex'})
df_dur_t_r_on = df_dur_t_on.rename(columns={0: "secondary somatosensory cortex",1: "secondary/primary somatosensory cortex",2:'primary somatosensory cortex',3:'primary motor cortex',4:'premotor cortex'})

df_dur_t_r_m = df_dur_t_r.assign(med_state='OFF')
df_dur_t_r_m_on = df_dur_t_r_on.assign(med_state='ON')

cdf_dur = pd.concat([df_dur_t_r_m,df_dur_t_r_m_on])
pd_burst_length = pd.melt(cdf_dur,id_vars=['med_state'],var_name=['channel'])

## M1 Probability of burst duration OFF vs ON (Pandas)
df_dur_4 = pd.DataFrame(burst_length_4)
df_dur_4_on = pd.DataFrame(burst_length_4_on) 

df_dur_4_m = df_dur_4.assign(Location ='ECOG_L4-L5_SMC_AT',Medication = 'OFF')
df_dur_4_m_on = df_dur_4_on.assign(Location ='ECOG_L4-L5_SMC_AT',Medication = 'ON')

df_dur_4_m_r = df_dur_4_m.rename(columns={0: "Burst Duration (s)"})
df_dur_4_m_r_on = df_dur_4_m_on.rename(columns={0: "Burst Duration (s)"})

pd_dur_4 = pd.concat([df_dur_4_m_r, df_dur_4_m_r_on])

## Histogram (Distribution of burst length) with range up to 10s
hist_dur_1, bins = np.histogram(burst_length_1,density=False, bins=100, range=(0, 10))
hist_dur_2, bins = np.histogram(burst_length_2,density=False, bins=100, range=(0, 10))
hist_dur_3, bins = np.histogram(burst_length_3,density=False, bins=100, range=(0, 10))
hist_dur_4, bins = np.histogram(burst_length_4,density=False, bins=100, range=(0, 10))
hist_dur_5, bins = np.histogram(burst_length_5,density=False, bins=100, range=(0, 10))

## Burst length probability of histogram
burst_length_normed_1 = 100*hist_dur_1 / burst_length_1.shape[0]
burst_length_normed_2 = 100*hist_dur_2 / burst_length_2.shape[0]
burst_length_normed_3 = 100*hist_dur_3 / burst_length_3.shape[0]
burst_length_normed_4 = 100*hist_dur_4 / burst_length_4.shape[0]
burst_length_normed_5 = 100*hist_dur_5 / burst_length_5.shape[0]

## (Grand) Mean Duration OFF vs ON 
mean_burst_length_1 = np.mean(burst_length_1)
mean_burst_length_2 = np.mean(burst_length_2)
mean_burst_length_3 = np.mean(burst_length_3)
mean_burst_length_4 = np.mean(burst_length_4)
mean_burst_length_5 = np.mean(burst_length_5)
print (mean_burst_length_4, mean_burst_length_4_on)

grand_mean = (mean_burst_length_1 + mean_burst_length_2 + mean_burst_length_3 + mean_burst_length_4 + mean_burst_length_5) /5 
grand_mean_on = (mean_burst_length_1_on + mean_burst_length_2_on + mean_burst_length_3_on + mean_burst_length_4_on + mean_burst_length_5_on) /5 
print (grand_mean, grand_mean_on) 

## Cortical Beta Burst Dynamic (Probability of different burst length) OFF vs ON (Pandas)
prob_high_dur_bursts_4=burst_length_normed_4[np.arange(12,100,1)].sum()
prob_high_dur_bursts_4_on=burst_length_normed_4_on[np.arange(12,100,1)].sum()

prob_low_dur_bursts_4 = burst_length_normed_4[np.arange(0,12)]
prob_low_dur_bursts_4_on = burst_length_normed_4_on[np.arange(0,12)]

burst_prob_dur_4 = np.append(prob_low_dur_bursts_4 ,prob_high_dur_bursts_4)
burst_prob_dur_4_on = np.append(prob_low_dur_bursts_4_on ,prob_high_dur_bursts_4_on)

bins_dur=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,'>1.2'] 

df_probdur_4 = pd.DataFrame(data=[bins_dur,burst_prob_dur_4]) 
df_probdur_4_on = pd.DataFrame(data=[bins_dur,burst_prob_dur_4_on]) 

df_probdur_t_4 =df_probdur_4.T
df_probdur_t_4_on =df_probdur_4_on.T

df_probdur_t_r_4 = df_probdur_t_4.rename(columns={0: "Burst Duration (s)",1:'Burst Probability (%)'})
df_probdur_t_r_4_on = df_probdur_t_4_on.rename(columns={0: "Burst Duration (s)",1:'Burst Probability (%)'})

df_probdur_t_r_m_4 = df_probdur_t_r_4.assign(Medication = 'OFF')
df_probdur_t_r_m_4_on = df_probdur_t_r_4_on.assign(Medication = 'ON')

pd_prob_dur_4 = pd.concat([df_probdur_t_r_m_4, df_probdur_t_r_m_4_on])


# 3.SAVING FEATURES IN A DICTIONARY #

# Normalized beta power OFF vs ON (vector):
## npow_1, npow_2, npow_3, npow_4, npow_5
# M1 normalized beta power Off and On (Pandas from npow_4)
## pw_c

# Burst duration of full beta Off & ON (vector): 
## burst_length_1, burst_length_2, burst_length_3, burst_length_4, burst_length_5 
# Burst duration in all channels ON vs OFF (Pandas from burst_length_1-5):
## pd_burst_length 
# M1 burst length Off vs On (vector)
## burst_length_4, burst_length_4_on
# M1 burst length Off and On (Pandas)
## pd_dur_4

# Histogram (Distribution of burst length) with range up to 10s Off & On (vector):
## hist_dur_1, hist_dur_2, hist_dur_3, hist_dur_4, hist_dur_5

# Burst length probability of histogram (vector) Off & ON
## burst_length_normed_1, burst_length_normed_2, burst_length_normed_3,       burst_length_normed_4, burst_length_normed_5

# (Grand) Mean burst duration OFF vs ON (integer)
## mean_burst_length_1, mean_burst_length_2, mean_burst_length_3, mean_burst_length_4, mean_burst_length_5
## mean_burst_length_4, mean_burst_length_4_on
## grand_mean, grand_mean_on

# Cortical Beta Burst Dynamics:
# M1 Probability of high duration bursts (>1.2s) (from burst_length_normed_4/_on) (vector)  
## prob_high_dur_bursts_4, prob_high_dur_bursts_4_on
# M1 Probability of low duration bursts (<1.2s) (from burst_length_normed_4/_on) (vector) 
## prob_low_dur_bursts_4, prob_low_dur_bursts_4_on
# M1 Probability of burst duration up to 10s Off vs On (vector)
## burst_prob_dur_4, burst_prob_dur_4_on
# M1 Probability of burst duration Off and On (Pandas)
## pd_prob_dur_4


# Plot biomarker comparison (beta power vs burst length) 

