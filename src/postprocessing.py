import pandas as pd
import numpy as np


def dataframe_mean_duration(mean_burst_duration):
    '''
    Structure feature in pandas
    '''
    pdur = pd.DataFrame(mean_burst_duration)
    pdur_r = pdur.rename(columns={0:'mean_burst_duration (s)'})
    return pdur_r

#def save_mean_duration(mean_burst_duration):
 #   mean_burst_duration.to_csv('mean_burst_duration.csv')

def dataframe_burst_duration(burst_duration):
    df_dur = pd.DataFrame(burst_duration)
    df_dur_t=df_dur.T
    df_dur_t_r = df_dur_t.rename(columns={0: "secondary somatosensory cortex",1: "secondary/primary somatosensory cortex",2:'primary somatosensory cortex',3:'primary motor cortex',4:'premotor cortex'})
    df_dur_t_r_m = df_dur_t_r.assign(med_state='OFF')
    #df_dur_t_r_m_on = df_dur_t_r_on.assign(med_state='ON')
   # cdf_dur = pd.concat([df_dur_t_r_m,df_dur_t_r_m_on])
    #pd_burst_length = pd.melt(cdf_dur,id_vars=['med_state'],var_name=['channel'])
    #return pd_burst_length

def dataframe_npow(power_spectra_norm):
    pw = pd.DataFrame(power_spectra_norm)
    #pw_on = pd.DataFrame(power_spectra_norm_on) 
    pw_a = pw.assign(Location='ECOG-L4-L5_SMC_AT', Medication = 'OFF')
    #pw_on_a = pw_on.assign(Location='ECOG-L4-L5_SMC_AT', Medication = 'ON')
    pw_r = pw_a.rename(columns={0:'Relative spectral power (au)'}) 
    #pw_r_on = pw_on_a.rename(columns={0:'Relative spectral power (au)'}) 
    #pw_c = pd.concat([pw_r, pw_r_on])
    #return pw_c

def dataframe_burst_dynamics(norm_histogram_duration):
    '''
    Structure Probability of M1 Burst Duration in Pandas
    '''
    bins_dur = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,'>1.2'] 
    prob_high_dur_bursts_M1=norm_histogram_duration[np.arange(12,100,1)].sum()
    prob_low_dur_bursts_M1 = norm_histogram_duration[np.arange(0,12)]
    burst_prob_dur_M1 = np.append(prob_low_dur_bursts_M1 ,prob_high_dur_bursts_M1)

    df_probdur_M1 = pd.DataFrame(data=[bins_dur,burst_prob_dur_M1])
    df_probdur_t_M1 =df_probdur_M1.T
    df_probdur_t_r_M1 = df_probdur_t_M1.rename(columns={0: "Burst Duration (s)",1:'Burst Probability (%)'})
    df_probdur_t_r_m_M1 = df_probdur_t_r_M1.assign(Medication = 'OFF')
    #df_probdur_t_r_m_M1_on = df_probdur_t_r_M1_on.assign(Medication = 'ON')
    #pd_prob_dur_M1 = pd.concat([df_probdur_t_r_m_M1, df_probdur_t_r_m_M1_on])
    #return pd_prob_dur_M1

def dataframe_burst_duration(burst_duration):
    df_dur_4 = pd.DataFrame(burst_duration)
    df_dur_4_m = df_dur_4.assign(Location ='ECOG_L4-L5_SMC_AT',Medication = 'OFF')
    df_dur_4_m_r = df_dur_4_m.rename(columns={0: "Burst Duration (s)"})
    #pd_dur_4 = pd.concat([df_dur_4_m_r, df_dur_4_m_r_on])
    #return pd_dur_4
