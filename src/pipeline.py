"""Pipelines for automated processing."""

import pathlib
import pandas as pd
from typing import Union

import numpy as np

from src import burst_calc, IO, postprocessing, preprocessing


def bursts_single_subject(
    path_run: Union[str, pathlib.Path],
    path_bids: Union[str, pathlib.Path],
    sub: str,
    m1: int,
    new_ch_names: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:

    raw, data, sfreq, line_freq = IO.read_BIDS_data(path_run, path_bids)
    raw_ecog = preprocessing.pick_ecog(raw)

    if sub == "001":
        raw_ecog_bi = preprocessing.bipolar_reference_s1(
            raw, raw_ecog, new_ch_names
        )
    else:
        raw_ecog_bi = preprocessing.bipolar_reference(
            raw, raw_ecog, new_ch_names
        )

    NUM_CH = len(raw_ecog_bi.get_channel_types())

    raw_ecog_filt = preprocessing.filtering(raw_ecog_bi)

    raw_ecog_dow = preprocessing.downsample(raw_ecog_filt)

    signal = preprocessing.get_data(raw_ecog_dow)

    stand_signal = preprocessing.z_score_signal(signal)

    run_TF = burst_calc.Time_Frequency_Estimation(stand_signal)

    # list of low, high, full beta bands for all channels
    l_beta = burst_calc.beta_bands(run_TF)

    # Averaging power in all beta bands
    l_beta_avg = [burst_calc.avg_power(l) for l in l_beta]

    # Z-Scored averaged beta traces
    l_beta_avg_norm = [burst_calc.z_score(l) for l in l_beta_avg]

    # 75th percentile of the power
    l_beta_thr = [
        burst_calc.percentile(l, percentile=75) for l in l_beta_avg_norm
    ]

    low = 0
    high = 1
    full = 2

    # 2. CALCULATING FEATURES (NORMALIZED POWER, BURST LENGTH, BURST DYNAMIC) AND BIOMARKER COMPARISON #
    # Power spectral density
    power_spectra = [
        np.nanmean(np.squeeze(run_TF[ch_idx, :, :]), axis=1)
        for ch_idx in range(len(raw_ecog_bi.get_channel_types()))
    ]
    # Normalized power spectral density
    power_spectra_norm = [
        p_ch / np.sum(p_ch[4:45] + p_ch[54:95]) for p_ch in power_spectra
    ]
    psd_M1 = power_spectra_norm[m1]

    # Burst duration
    burst_duration = [
        burst_calc.get_burst_length(l, l_beta_thr[full][idx], sfreq=200)
        for idx, l in enumerate(l_beta_avg_norm[full])
    ]
    burst_duration_cl = [
        burst_calc.exclude_short_bursts(burst_duration[ch_idx])
        for ch_idx in range(NUM_CH)
    ]
    burst_duration_cl_m1 = burst_duration_cl[m1]
    # Mean burst duration
    mean_burst_duration = [
        np.nanmean(burst_duration_cl[ch_idx], axis=0)
        for ch_idx in range(NUM_CH)
    ]
    mean_dur_m1 = mean_burst_duration[m1]

    # Histogram of burst duration
    histogram_duration = [
        np.histogram(
            burst_duration_cl[ch_idx], density=False, bins=20, range=(0, 2)
        )[0]
        for ch_idx in range(NUM_CH)
    ]
    hist_dur_m1 = histogram_duration[m1]
    # Normed Histogram
    n_hist_dur = [
        100 * histogram_duration[ch_idx] / len(burst_duration_cl[ch_idx])
        for ch_idx in range(NUM_CH)
    ]
    n_hist_dur_m1 = n_hist_dur[m1]
    n_hist_dur_m1_cl = np.delete(n_hist_dur_m1, 0)
    short_bursts = n_hist_dur_m1_cl[:7]
    prol_bursts = np.sum(n_hist_dur_m1_cl[7:])
    normhist_dur_m1 = np.append(short_bursts, prol_bursts)

    # Burst Amplitude
    burst_amplitude = [
        burst_calc.get_mean_burst_amplitude(l, l_beta_thr[full][idx])
        for idx, l in enumerate(l_beta_avg_norm[full])
    ]
    burst_amplitude_m1 = burst_amplitude[m1]

    # Burst Rate
    burst_rate = [
        np.sum(histogram_duration[ch_idx] / raw.times[-1])
        for ch_idx in range(len(raw_ecog_bi.get_channel_types()))
    ]
    burst_rate_m1 = burst_rate[m1]

    # 3. STRUCTURE FEATURES #
    # Burst Features
    burst_char_pd = postprocessing.dataframe_burst_char(
        mean_dur_m1, burst_amplitude_m1, burst_rate_m1
    )

    # M1 Beta Burst Dynamics
    M1_burst_dynamics = postprocessing.dataframe_burst_dynamics(
        normhist_dur_m1
    )

    # normalized beta power
    npow = postprocessing.dataframe_npow(psd_M1)

    return burst_char_pd, M1_burst_dynamics, npow
