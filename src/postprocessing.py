import pandas as pd
import numpy as np


def dataframe_burst_char(mean_burst_duration_M1,burst_amplitude_M1,burst_rate_M1):
    '''
    Structure feature in pandas
    '''
    pdburst = pd.DataFrame({'Subject':9, 'Medication':'OFF','Mean Burst Duration (s)':mean_burst_duration_M1,'Mean Burst Amplitude (au)':burst_amplitude_M1,'Burst Rate': burst_rate_M1} ,index=['Run 1'])
    return pdburst

def dataframe_burst_dynamics(norm_histogram_duration):
    df_probdur_M1 = pd.DataFrame(norm_histogram_duration)
    df_probdur_t_M1 = df_probdur_M1.T
    df_his = df_probdur_t_M1.assign( Subject= 9 , Medication = 'OFF', Run= 1 )
    return df_his

def dataframe_npow(power_spectra_norm):
    pw = pd.DataFrame(power_spectra_norm)
    pw_t = pw.T
    pw_a = pw_t.assign( Subject= 9, Medication = 'OFF', Run= 1 )
    return pw_a
