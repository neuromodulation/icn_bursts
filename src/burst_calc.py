from os import stat
import numpy as np
from scipy import stats
import mne

LOW_BETA = (12, 20)
HIGH_BETA = (19, 35)
FULL_BETA = (12, 35)


def Time_Frequency_Estimation(signal):
    freqs = np.arange(1,100)
    power = mne.decoding.TimeFrequency(freqs, sfreq=250, method='morlet', n_cycles=10, output='power', )
    run_TF = power.transform(signal)
    return (run_TF)

def beta_bands(run_TF):
    '''
    Beta bands of the ecog channels: low beta(13-20Hz), high beta (20-35Hz), full beta (13-35Hz)
    '''
    l_low_beta = []
    l_high_beta = []
    l_full_beta = []
    for ch_idx in range(run_TF.shape[0]):
        l_low_beta.append(run_TF[ch_idx, LOW_BETA[0]:LOW_BETA[1],:])
        l_high_beta.append(run_TF[ch_idx, HIGH_BETA[0]:HIGH_BETA[1],:])
        l_full_beta.append(run_TF[ch_idx, FULL_BETA[0]:FULL_BETA[1],:])

    return l_low_beta, l_high_beta, l_full_beta

def avg_power(l_beta):
    return [np.mean(l_ch, axis=0) for l_ch in l_beta]

def z_score(l_beta):
    return [stats.zscore(l_ch, axis=0) for l_ch in l_beta]

def percentile(l_beta, percentile):
    return [np.percentile(l_ch, q=percentile) for l_ch in l_beta]


def get_burst_length(beta_averp_norm,beta_thr, sfreq=250):
    """
    Characterization of beta bursts: Analysing the duration of beta burst 
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

def burst_amplitude(beta_averp_norm,beta_thr, sfreq=250):
    '''
    mean amplitude of bursts across recording
    '''
    deriv = np.diff (beta_averp_norm >= beta_thr) 
    isburst = False
    burst_amplitude = []
    burst_start = 0

    for index, i in enumerate(deriv):
        if i == True:
            if isburst == True:
                burst_amplitude.append(index - burst_start)

                isburst = False
            else:
                burst_start = index
                isburst = True
    burst_length = np.array(burst_length)/sfreq
    
    return burst_amplitude

def burst_rate(beta_averp_norm,beta_thr, sfreq=250):
    '''
    calc burst rate of channel in recording
    '''
    