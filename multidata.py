
# 1.READ IN THE DATA #

#import libraries and modules
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

# Find all StimOff Rest Files (MedOff & MedON)
## Initiliaze the layout
data_path = os.path.join('/Users/alidzaye/rawdata')
layout = BIDSLayout(data_path)
print(layout)

## Rest data OFF & ON StimOff
files = layout.get(extension='vhdr', task='Rest', acquisition='StimOff', return_type='filename')
files_off = layout.get(extension='vhdr', task='Rest', acquisition='StimOff', 
                    session=['EphysMedOff01','EphysMedOff02','EphysMedOff03'], return_type='filename')
files_on = layout.get(extension='vhdr', task='Rest', session=['EphysMedOn01','EphysMedOn02','EphysMedOn03'],
                     acquisition='StimOff',     return_type='filename')
print(len(files))
print(len(files_off))
print(len(files_on))

#read the files with mne Bids
def read_BIDS_data(PATH_RUN, BIDS_PATH):
    """Given a run path and bids data path, read the respective data
    Parameters
    ----------
    PATH_RUN : string
    BIDS_PATH : string
    Returns
    -------
    raw_arr : mne.io.RawArray
    raw_arr_data : np.ndarray
    fs : int
    line_noise : int
    """
    For i in range(len(files)): 
    entities = mne_bids.get_entities_from_fname(PATH_RUN)

    bids_path = mne_bids.BIDSPath(
            subject=entities["subject"],
            session=entities["session"],
            task=entities["task"],
            run=entities["run"],
            acquisition=entities["acquisition"],
            datatype="ieeg",
            root=BIDS_PATH,
                            )

    raw_arr = mne_bids.read_raw_bids(bids_path)
    return (
        raw_arr,
        raw_arr.get_data(),
        int(np.ceil(raw_arr.info["sfreq"])),
        int(raw_arr.info["line_freq"]),),

PATH_BIDS = r'/Users/alidzaye/rawdata'
PATH_RUN = r'files[i]'

raw, dat, sfreq, line_freq = read_BIDS_data(PATH_RUN, PATH_BIDS)

# Preprocessing
def pick_ecog(raw):
    '''
    pick ECoG channels
    '''
    raw_ecog = []
    For i in range (len(raw)):
    raw_ecog.append(raw.pick_types(ecog=True).ch_names)

    return raw_ecog
raw_ecog = pick_ecog(raw)




#Next Steps: 



## bipolar re-reference
new_ch_names = ['ECOG_L_1_SMC_BI',
               'ECOG_L_2_SMC_BI',
               'ECOG_L_3_SMC_BI',
               'ECOG_L_4_SMC_BI',
              'ECOG_L_5_SMC_BI']
anode = raw_ecog.ch_names[0:5]
cathode = raw_ecog.ch_names[1:6]
raw_ecog_bi = mne.set_bipolar_reference(raw_ecog.load_data(), anode=anode,
                                        cathode=cathode, ch_name=new_ch_names )

anode_on = raw_ecog_on.ch_names[0:5]
cathode_on = raw_ecog_on.ch_names[1:6]
raw_ecog_bi_on = mne.set_bipolar_reference(raw_ecog_on.load_data(), anode=anode_on,
                                        cathode=cathode_on, ch_name=new_ch_names )

## Filtering (HP 3, NF 50,251,50, LP 250)
raw_ecog_hi = raw_ecog_bi.copy().filter(3, None,)
raw_ecog_hi_lo = raw_ecog_hi.copy().filter(None, 250)
raw_ecog_hi_lo_nf = raw_ecog_hi_lo.copy().notch_filter(np.arange(50,251,50), filter_length="auto", phase='zero')

raw_ecog_hi_on = raw_ecog_bi_on.copy().filter(3, None,)
raw_ecog_hi_lo_on = raw_ecog_hi_on.copy().filter(None, 250)
raw_ecog_hi_lo_nf_on = raw_ecog_hi_lo_on.copy().notch_filter(np.arange(50,251,50), filter_length="auto", phase='zero')

##Artefact Detection
# plot filtered ecog channels for annotiations
#%matplotlib qt
#raw_ecog_hi_lo_nf.plot(scalings='auto', highpass=3, lowpass=95, decim='auto')

####Cropping the last bit of data to ignore artefacts at the end
raw_ecog_cropped = raw_ecog_hi_lo_nf.copy().crop(tmax=618)

##Downsample Data to 250Hz for faster processing
raw_ecog_dow = raw_ecog_cropped.copy().resample(250)

## get the data with the function
signal = raw_ecog_dow.copy().get_data()

## z-score the data
stand_raw_ecog = stats.zscore(signal, axis=1)

## Time Frequency estimation
freqs = np.arange(1,100)
power = mne.decoding.TimeFrequency(freqs, sfreq=250, method='morlet', n_cycles=10, output='power', )
run_TF = power.transform(stand_raw_ecog)

## Beta bands of the ecog channels: low beta(13-20Hz), high beta (20-35Hz), full beta (13-35Hz)
low_beta_1_averp = np.mean(low_beta_1, axis=0)
high_beta_1_averp = np.mean(high_beta_1, axis=0)
full_beta_1_averp = np.mean(full_beta_1, axis=0)

low_beta_2_averp = np.mean(low_beta_2, axis=0)
high_beta_2_averp = np.mean(high_beta_2, axis=0)
full_beta_2_averp = np.mean(full_beta_2, axis=0)

low_beta_3_averp = np.mean(low_beta_3, axis=0)
high_beta_3_averp = np.mean(high_beta_3, axis=0)
full_beta_3_averp = np.mean(full_beta_3, axis=0)

low_beta_4_averp = np.mean(low_beta_4, axis=0)
high_beta_4_averp = np.mean(high_beta_4, axis=0)
full_beta_4_averp = np.mean(full_beta_4, axis=0)

low_beta_5_averp = np.mean(low_beta_5, axis=0)
high_beta_5_averp = np.mean(high_beta_5, axis=0)
full_beta_5_averp = np.mean(full_beta_5, axis=0)

## Z-Scored averaged beta traces
low_beta_1_averp_norm = stats.zscore(low_beta_1_averp, axis=0)
high_beta_1_averp_norm = stats.zscore(high_beta_1_averp, axis=0)
full_beta_1_averp_norm = stats.zscore(high_beta_1_averp, axis=0)

low_beta_2_averp_norm = stats.zscore(low_beta_2_averp, axis=0)
high_beta_2_averp_norm = stats.zscore(high_beta_2_averp, axis=0)
full_beta_2_averp_norm = stats.zscore(high_beta_2_averp, axis=0)

low_beta_3_averp_norm = stats.zscore(low_beta_3_averp, axis=0)
high_beta_3_averp_norm = stats.zscore(high_beta_3_averp, axis=0)
full_beta_3_averp_norm = stats.zscore(high_beta_3_averp, axis=0)

low_beta_4_averp_norm = stats.zscore(low_beta_4_averp, axis=0)
high_beta_4_averp_norm = stats.zscore(high_beta_4_averp, axis=0)
full_beta_4_averp_norm = stats.zscore(high_beta_4_averp, axis=0)

low_beta_5_averp_norm = stats.zscore(low_beta_5_averp, axis=0)
high_beta_5_averp_norm = stats.zscore(high_beta_5_averp, axis=0)
full_beta_5_averp_norm = stats.zscore(high_beta_5_averp, axis=0)

## 75th percentile of the power
low_beta_1_thr = np.percentile(low_beta_1_averp_norm, 75)
high_beta_1_thr = np.percentile(high_beta_1_averp_norm, 75)
full_beta_1_thr = np.percentile(full_beta_1_averp_norm, 75)

low_beta_2_thr = np.percentile(low_beta_2_averp_norm, 75)
high_beta_2_thr = np.percentile(high_beta_2_averp_norm, 75)
full_beta_2_thr = np.percentile(full_beta_2_averp_norm, 75)

low_beta_3_thr = np.percentile(low_beta_3_averp_norm, 75)
high_beta_3_thr = np.percentile(high_beta_3_averp_norm, 75)
full_beta_3_thr = np.percentile(full_beta_3_averp_norm, 75)

low_beta_4_thr = np.percentile(low_beta_4_averp_norm, 75)
high_beta_4_thr = np.percentile(high_beta_4_averp_norm, 75)
full_beta_4_thr = np.percentile(full_beta_4_averp_norm, 75)

low_beta_5_thr = np.percentile(low_beta_5_averp_norm, 75)
high_beta_5_thr = np.percentile(high_beta_5_averp_norm, 75)
full_beta_5_thr = np.percentile(full_beta_5_averp_norm, 75)

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



# 4. PlOTTING FEATURES FOR EVERY RUN #

# M1 burst length plot
sns.set(style="white", font_scale=1)
plt.hist(burst_length_4, bins=13, range=(0, 1.3))
sns.despine()

# Plot beta power vs burst length across channels
sns.set(style="white", font_scale=1.2)
fig = plt.figure(figsize=(25,15))

ax1 = plt.subplot2grid((2, 5), (0, 0),colspan=1) 
plt.yticks(np.arange(0, 0.2, step=0.05))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (au)')
ax2 = plt.subplot2grid((2, 5), (0, 1),colspan=1)
plt.yticks(np.arange(0, 0.2, step=0.05))
ax3 = plt.subplot2grid((2, 5), (0, 2),colspan=1) 
plt.yticks(np.arange(0, 0.2, step=0.05))
ax4 = plt.subplot2grid((2, 5), (0, 3),colspan=1)
plt.yticks(np.arange(0, 0.2, step=0.05))
ax5 = plt.subplot2grid((2, 5), (0, 4),colspan=1)
plt.yticks(np.arange(0, 0.2, step=0.05))

ax1.set_ylim(0,0.2)
ax2.set_ylim(0,0.2)
ax3.set_ylim(0,0.2)
ax4.set_ylim(0,0.2)
ax5.set_ylim(0,0.2)

ax1.set_xlim(0,60)
ax2.set_xlim(0,60)
ax3.set_xlim(0,60)
ax4.set_xlim(0,60)
ax5.set_xlim(0,60)

ax1.plot(freqs,npow_1,label= 'OFF Medication')
ax1.plot(freqs,npow_1_on,label= 'ON Medication')
ax2.plot(freqs,npow_2,label= 'OFF Medication')
ax2.plot(freqs,npow_2_on,label= 'ON Medication')
ax3.plot(freqs,npow_3,label= 'OFF Medication')
ax3.plot(freqs,npow_3_on,label= 'ON Medication')
ax4.plot(freqs,npow_4,label= 'OFF Medication')
ax4.plot(freqs,npow_4_on,label= 'ON Medication')
ax5.plot(freqs,npow_5,label= 'OFF Medication')
ax5.plot(freqs,npow_5_on,label= 'ON Medication')
plt.legend(bbox_to_anchor=(1.05, 1),loc=1, borderaxespad=0)
ax7 = plt.subplot2grid((2, 6), (1,0),colspan=10) 

alpha_box = 0.4
ax7=sns.boxplot(x='channel', y='value', hue='med_state',data=pd_burst_length, palette="viridis", 
            boxprops=dict(alpha=alpha_box),
           showfliers=False,
           whiskerprops={'linewidth':2, "zorder":10, "alpha":alpha_box},
           capprops={"alpha":alpha_box},
           medianprops=dict(linestyle='-.', linewidth=5, color="grey", alpha=alpha_box))
   
ax7 = sns.stripplot(x='channel', y='value', hue='med_state', 
             data=pd_burst_length,palette="viridis", dodge=True, s=5)

plt.ylabel('burst duration (s)')
plt.xlabel('')

plt.suptitle(' Beta Power vs Burst Duration ECoG Berlin OFF and ON Sub003 Run01 Rest ')
sns.despine()



# Plot biomarker comparison (beta power vs burst length) 
sns.set(style="white", font_scale=1.3)
fig,ax = plt.subplots(1,3, figsize=(25,15),)

plt.subplot(131)
plt.plot(freqs,npow_4,label= 'OFF ',linewidth=4)
plt.plot(freqs,npow_4_on,label= 'ON',linewidth=4)
plt.xlim(0,60)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Relative spectral power (au)')
plt.legend(title='Medication', fontsize=15,title_fontsize=15)
        
plt.subplot(132)           
alpha_box=0.3
sns.barplot(data=pd_prob_dur_4, x='Burst Duration (s)', y='Burst Probability (%)', hue='Medication') 
plt.legend(title='Medication', fontsize=15,title_fontsize=15)

plt.subplot(133)
alpha_box = 0.4
g = sns.boxplot(x='Location', y='Burst Duration (s)', hue='Medication',data=pd_dur_4,         
           showfliers=False,meanline=dict(color='r'), showmeans=True,
           whiskerprops={'linewidth':2, "zorder":10, "alpha":alpha_box},
           capprops={"alpha":alpha_box},
           meanprops=dict(linestyle='-.', linewidth=5,color='r'))
plt.xlabel('Primary Motor Cortex')
plt.legend(title='Medication', fontsize=15,title_fontsize=15)

for n, ax in enumerate(ax):   
    ax.text(-0.1, 1.1, string.ascii_uppercase[n], transform=ax.transAxes, 
            size=30, weight='bold')
    
sns.despine()
