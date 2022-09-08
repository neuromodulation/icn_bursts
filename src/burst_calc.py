from os import stat
import numpy as np
from scipy import stats
import mne

LOW_BETA = (13, 21)
HIGH_BETA = (20, 36)
FULL_BETA = (13, 36)
mu_beta = (7,9)


def Time_Frequency_Estimation(signal):
    freqs = np.arange(1, 101)
    power = mne.decoding.TimeFrequency(
        freqs, sfreq=250, method="morlet", n_cycles=10, output="power"
    )
    run_TF = power.transform(signal)
    return run_TF


def beta_bands(run_TF):
    """
    Beta bands of the ecog channels: low beta(13-20Hz), high beta (20-35Hz), full beta (13-35Hz)
    """
    l_low_beta = []
    l_high_beta = []
    l_full_beta = []
    l_mu_beta = []
    for ch_idx in range(run_TF.shape[0]):
        l_low_beta.append(run_TF[ch_idx, LOW_BETA[0] : LOW_BETA[1], :])
        l_high_beta.append(run_TF[ch_idx, HIGH_BETA[0] : HIGH_BETA[1], :])
        l_full_beta.append(run_TF[ch_idx, FULL_BETA[0] : FULL_BETA[1], :])
        l_mu_beta.append(run_TF[ch_idx, mu_beta[0] : mu_beta[1], :])

    return l_low_beta, l_high_beta, l_full_beta, l_mu_beta


def avg_power(l_beta):
    return [np.mean(l_ch, axis=0) for l_ch in l_beta]


def z_score(l_beta):
    return [stats.zscore(l_ch, axis=0) for l_ch in l_beta]


def percentile(l_beta, percentile):
    return [np.percentile(l_ch, q=percentile) for l_ch in l_beta]


def get_burst_length(beta_averp_norm, beta_thr, sfreq=250):
    """
    Analysing the duration of beta burst 
    """
    bursts = np.zeros((beta_averp_norm.shape[0] + 1), dtype=bool)
    bursts[1:] = beta_averp_norm >= beta_thr
    deriv = np.diff(bursts)
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
    if isburst:
        burst_length.append(index + 1 - burst_start)
    burst_length = np.array(burst_length) / sfreq

    return burst_length


def exclude_short_bursts(burst_length):
    """
    exclude bursts shorter than 100ms
    """
    return [i for i in burst_length if i >= 0.1]


def get_burst_amplitude(beta_amplitude, beta_thr):
    amplitude = []
    no_bursts = True
    cont = False
    for val in beta_amplitude:
        if val >= beta_thr:
            no_bursts = False
            if cont == False:
                burst = [val]
                cont = True
            else:
                burst.append(val)
        else:
            if not no_bursts:
                cont = False
                amplitude.append(burst)
    mean_amplitude_single_burst = [np.mean(burst) for burst in amplitude]
    mean_amplitude = np.mean(mean_amplitude_single_burst)

    return mean_amplitude

