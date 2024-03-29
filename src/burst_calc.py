from os import stat
import numpy as np
from scipy import stats
import mne
import numpy


def Time_Frequency_Estimation(signal):
    freqs = np.arange(1, 101)
    power = mne.decoding.TimeFrequency(
        freqs, sfreq=1600, method="morlet", n_cycles=10, output="power"
    )
    run_TF = power.transform(signal)
    return run_TF


def beta_bands(run_TF):
    """
    Beta bands of the ecog channels: low beta(13-20Hz), high beta (20-35Hz), full beta (13-35Hz)
    """
    THETA = (4, 9)
    MU = (8, 13)
    LOW_BETA = (13, 21)
    HIGH_BETA = (20, 36)
    FULL_BETA = (13, 36)

    l_theta = []
    l_mu = []
    l_low_beta = []
    l_high_beta = []
    l_full_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, THETA[0] : THETA[1], :])
        l_mu.append(run_TF[ch_idx, MU[0] : MU[1], :])
        l_low_beta.append(run_TF[ch_idx, LOW_BETA[0] : LOW_BETA[1], :])
        l_high_beta.append(run_TF[ch_idx, HIGH_BETA[0] : HIGH_BETA[1], :])
        l_full_beta.append(run_TF[ch_idx, FULL_BETA[0] : FULL_BETA[1], :])


    return l_theta, l_mu, l_low_beta, l_high_beta, l_full_beta

def beta_bands_sub3(run_TF):
    indTHETA = (5, 8)
    indBETA = (19, 22)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub3_on(run_TF):
    indTHETA = (4, 7)
    indBETA = (11, 14)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub4(run_TF):
    indTHETA = (4, 7)
    indBETA = (13, 16)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub4_on(run_TF):
    indTHETA = (4, 7)
    indBETA = (25, 28)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub5(run_TF):
    indTHETA = (5, 8)
    indBETA = (14, 17)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub5_on(run_TF):
    indTHETA = (4, 7)
    indBETA = (14, 17)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub6(run_TF):
    indTHETA = (4, 7)
    indBETA = (24, 27)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub7(run_TF):
    indTHETA = (4, 7)
    indBETA = (20, 23)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub7_on(run_TF):
    indTHETA = (5, 8)
    indBETA = (20, 23)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub8(run_TF):
    indTHETA = (4, 7)
    indBETA = (15, 18)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub8_on(run_TF):
    indTHETA = (6, 9)
    indBETA = (12, 15)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub9(run_TF):
    indTHETA = (9, 12)
    indBETA = (18, 21)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub9_on(run_TF):
    indTHETA = (8, 11)
    indBETA = (16, 19)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub11(run_TF):
    indTHETA = (7, 10)
    indBETA = (16, 19)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub11_on(run_TF):
    indTHETA = (7, 10)
    indBETA = (17, 20)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub12(run_TF):
    indTHETA = (9, 12)
    indBETA = (22, 25)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub12_on(run_TF):
    indTHETA = (6, 9)
    indBETA = (23, 26)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub13(run_TF):
    indTHETA = (7, 10)
    indBETA = (22, 25)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub13_on(run_TF):
    indTHETA = (7, 10)
    indBETA = (23, 26)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub14(run_TF):
    indTHETA = (4, 7)
    indBETA = (19, 22)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub14_on(run_TF):
    indTHETA = (8, 11)
    indBETA = (19, 22)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub15(run_TF):
    indTHETA = (4, 7)
    indBETA = (16, 19)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def beta_bands_sub15_on(run_TF):
    indTHETA = (4, 7)
    indBETA = (20, 23)

    l_theta = []
    l_beta = []

    for ch_idx in range(run_TF.shape[0]):
        l_theta.append(run_TF[ch_idx, indTHETA[0] : indTHETA[1], :])
        l_beta.append(run_TF[ch_idx, indBETA[0] :indBETA[1], :])

    return l_theta, l_beta

def avg_power(l_beta):
    return [np.mean(l_ch, axis=0) for l_ch in l_beta]


def z_score(l_beta):
    return [stats.zscore(l_ch, axis=0) for l_ch in l_beta]


def percentile(l_beta, percentile):
    return [np.percentile(l_beta, q=percentile)]  # for l_ch in l_beta]


def get_burst_length(beta_averp_norm, beta_thr, sfreq):
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

def smooth(array, window_size=320):
    kernel = np.ones(window_size) / window_size
    data_convolved = np.convolve(array, kernel, mode='same')
    return data_convolved
