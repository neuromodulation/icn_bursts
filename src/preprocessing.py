import numpy as np
import mne
from scipy import stats


def pick_ecog(raw):
    '''
    pick ECoG channels
    '''
    raw_ecog = []
    raw_ecog.append(raw.pick_types(ecog=True).ch_names)

    return raw_ecog

def bipolar_reference (raw, raw_ecog, new_ch_names):
    
    anode = raw_ecog[0][0:5]
    cathode = raw_ecog[0][1:6]
    raw_ecog_bi = mne.set_bipolar_reference(raw.load_data(), anode=anode,
                                        cathode=cathode, ch_name=new_ch_names )
    return (raw_ecog_bi)

def filtering (raw_ecog_bi):
    '''
    Filtering (Highpass 3 Hz, Notchfilter 50,251,50Hz, Lowpass 250Hz)
    '''
    raw_ecog_hi = raw_ecog_bi.copy().filter(3, None,)
    raw_ecog_hi_lo = raw_ecog_hi.copy().filter(None, 250)
    raw_ecog_filt = raw_ecog_hi_lo.copy().notch_filter(np.arange(50,251,50), filter_length="auto", phase='zero')
    return(raw_ecog_filt)

def downsample(raw_ecog_filt):
    '''
    Downsample Data to 250Hz for faster processing
    '''
    raw_ecog_dow = raw_ecog_filt.copy().resample(250)
    return (raw_ecog_dow)

def get_data (raw_ecog_dow):
    signal = raw_ecog_dow.copy().get_data()
    return (signal)

def z_score_signal(signal):
    stand_signal = stats.zscore(signal, axis=1)
    return (stand_signal)