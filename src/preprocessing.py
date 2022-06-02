import numpy as np
import mne
from scipy import stats


def pick_ecog(raw):
    """
    pick ECoG channels
    """
    raw_ecog = []
    raw_ecog.append(raw.pick_types(ecog=True).ch_names)
    raw_ecog_red = raw_ecog[0][0:6]
    return raw_ecog_red


def bipolar_reference(raw, raw_ecog, new_ch_names):

    anode = raw_ecog[0:5]
    cathode = raw_ecog[1:6]
    raw_ecog_bi = mne.set_bipolar_reference(
        raw.load_data(), anode=anode, cathode=cathode, ch_name=new_ch_names
    )
    return raw_ecog_bi


def bipolar_reference_s1(raw, raw_ecog, new_ch_names):

    anode = raw_ecog[0:4]
    cathode = raw_ecog[1:5]
    raw_ecog_bi = mne.set_bipolar_reference(
        raw.load_data(), anode=anode, cathode=cathode, ch_name=new_ch_names
    )
    # raw_ecog_bi = raw_ecog_bi.load_data().add_channels(
    #   [raw.pick_channels(["ECOG_L_1_2_SMC_AT"])], force_update_info=True
    # )
    # channel_order = [
    #    "ECOG_L_1_2_SMC_AT",
    #    "ECOG_L_2_3_SMC_AT",
    #    "ECOG_L_3_4_SMC_AT",
    #    "ECOG_L_4_5_SMC_AT",
    #    "ECOG_L_5_6_SMC_AT",
    # ]
    # raw_ecog_bi = raw_ecog_bi.reorder_channels(channel_order)
    return raw_ecog_bi


def bipolar_reference_s10_on(raw, raw_ecog, new_ch_names):
    anode = raw_ecog[0:4]
    cathode = raw_ecog[1:5]
    raw_ecog_bi = mne.set_bipolar_reference(
        raw.load_data(), anode=anode, cathode=cathode, ch_name=new_ch_names
    )
    return raw_ecog_bi


def filtering(raw_ecog_bi):
    """
    Filtering (Highpass 3 Hz, Notchfilter 50,251,50Hz, Lowpass 250Hz)
    """
    raw_ecog_hi = raw_ecog_bi.copy().filter(3, None,)
    raw_ecog_hi_lo = raw_ecog_hi.copy().filter(None, 250)
    raw_ecog_filt = raw_ecog_hi_lo.copy().notch_filter(
        np.arange(50, 251, 50), filter_length="auto", phase="zero"
    )
    return raw_ecog_filt


def downsample(raw_ecog_filt):
    """
    Downsample Data to 1600Hz for faster processing
    """
    raw_ecog_dow = raw_ecog_filt.copy().resample(1600)
    return raw_ecog_dow


def get_data(raw_ecog_dow):
    signal = raw_ecog_dow.copy().get_data()
    return signal


def z_score_signal(signal):
    stand_signal = stats.zscore(signal, axis=1)
    return stand_signal

