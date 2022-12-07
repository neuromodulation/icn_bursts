from os import stat
import numpy as np
from scipy import stats
import mne
import numpy


def Time_Frequency_Estimation(signal):
    freqs = np.arange(1, 101)
    power = mne.decoding.TimeFrequency(
        freqs, sfreq=250, method="morlet", n_cycles=10, output="power"
    )
    run_TF = power.transform(signal)
    return run_TF


def beta_bands_sub3(run_TF):
    """
    Beta bands of the ecog channels: low beta(13-20Hz), high beta (20-35Hz), full beta (13-35Hz)
    """
    THETA = (7, 9)
    MU = (8, 11)
    LOW_BETA = (15, 18)
    HIGH_BETA = (21, 24)
    FULL_BETA = (15, 18)

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


def beta_bands_sub4(run_TF):
    THETA = (7, 9)
    MU = (8, 11)
    LOW_BETA = (14, 17)
    HIGH_BETA = (27, 30)
    FULL_BETA = (14, 17)

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


def beta_bands_sub5(run_TF):
    THETA = (5, 8)
    MU = (8, 11)
    LOW_BETA = (16, 19)
    HIGH_BETA = (27, 30)
    FULL_BETA = (16, 19)

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


def beta_bands_sub6(run_TF):
    THETA = (5, 8)
    MU = (8, 11)
    LOW_BETA = (15, 18)
    HIGH_BETA = (25, 28)
    FULL_BETA = (25, 28)

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


def beta_bands_sub7(run_TF):
    THETA = (4, 7)
    MU = (8, 11)
    LOW_BETA = (12, 15)
    HIGH_BETA = (21, 24)
    FULL_BETA = (21, 24)

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


def beta_bands_sub8(run_TF):
    THETA = (5, 8)
    MU = (8, 11)
    LOW_BETA = (15, 18)
    HIGH_BETA = (20, 23)
    FULL_BETA = (15, 18)

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


def beta_bands_sub9(run_TF):
    THETA = (6, 9)
    MU = (9, 12)
    LOW_BETA = (17, 20)
    HIGH_BETA = (20, 23)
    FULL_BETA = (20, 23)

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


def beta_bands_sub11(run_TF):
    THETA = (4, 7)
    MU = (11, 13)
    LOW_BETA = (13, 16)
    HIGH_BETA = (26, 29)
    FULL_BETA = (13, 16)

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


def beta_bands_sub12(run_TF):
    THETA = (4, 7)
    MU = (8, 11)
    LOW_BETA = (18, 21)
    HIGH_BETA = (23, 26)
    FULL_BETA = (23, 26)

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


def beta_bands_sub13(run_TF):
    THETA = (6, 9)
    MU = (8, 11)
    LOW_BETA = (14, 17)
    HIGH_BETA = (23, 26)
    FULL_BETA = (14, 17)

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


def beta_bands_sub14(run_TF):
    THETA = (4, 7)
    MU = (10, 13)
    LOW_BETA = (18, 21)
    HIGH_BETA = (20, 23)
    FULL_BETA = (20, 23)

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


def beta_bands_sub15(run_TF):
    THETA = (6, 9)
    MU = (8, 11)
    LOW_BETA = (18, 21)
    HIGH_BETA = (21, 24)
    FULL_BETA = (21, 24)

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


def avg_power(l_beta):
    return [np.mean(l_ch, axis=0) for l_ch in l_beta]


def z_score(l_beta):
    return [stats.zscore(l_ch, axis=0) for l_ch in l_beta]


def percentile(l_beta, percentile):
    return [np.percentile(l_beta, q=percentile)]  # for l_ch in l_beta]


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


def smooth(x, window_len=50, window="hanning"):
    """smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)
    
    see also: 
    
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
 
    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    # if x.ndim != 1:
    #    raise ValueError, "smooth only accepts 1 dimension arrays."

    # if x.size < window_len:
    #   raise ValueError, "Input vector needs to be bigger than window size."

    if window_len < 3:
        return x

    # if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
    #   raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"

    s = numpy.r_[x[window_len - 1 : 0 : -1], x, x[-2 : -window_len - 1 : -1]]
    # print(len(s))
    if window == "flat":  # moving average
        w = numpy.ones(window_len, "d")
    else:
        w = eval("numpy." + window + "(window_len)")

    y = numpy.convolve(w / w.sum(), s, mode="valid")
    return y

