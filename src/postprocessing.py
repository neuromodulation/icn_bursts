import pandas as pd
import numpy as np


def dataframe_burst_char(mean_burst_duration_M1,burst_amplitude_M1,burst_rate_M1):
    '''
    Structure feature in pandas
    '''
    pdburst = pd.DataFrame({'Duration':mean_burst_duration_M1,'Amplitude':burst_amplitude_M1,'Rate': burst_rate_M1},index=[0])
    return pdburst

def dataframe_burst_dynamics(norm_histogram_duration):
    df_probdur_M1 = pd.DataFrame(norm_histogram_duration)
    df_probdur_t_M1 = df_probdur_M1.T
   # df_his = df_probdur_t_M1.assign( Subject= 'X' , Medication = 'X', Run= 'X' )
    return df_probdur_t_M1

def dataframe_npow(power_spectra_norm):
    pw = pd.DataFrame(power_spectra_norm)
    pw_t = pw.T
    #pw_a = pw_t.assign( Subject= 'X', Medication = 'X', Run= 'X' )
    return pw_t
