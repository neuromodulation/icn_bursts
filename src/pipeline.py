"""Pipelines for automated processing."""

import pathlib
import pandas as pd
import mne
from typing import Union
import seaborn as sns
from matplotlib import pyplot as plt

import numpy as np

from src import burst_calc, IO, postprocessing, preprocessing


def bursts_single_run(
    path_run: Union[str, pathlib.Path],
    path_bids: Union[str, pathlib.Path],
    sub: str,
    m1: int,
    new_ch_names: list[str],
    med: list[str],
    session: str,
    task: str,
    acquisition: str,
    run: str,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:

    raw, data, sfreq, line_freq = IO.read_BIDS_data(path_run, path_bids)
    annotations = mne.read_annotations(
        preprocessing.generate_annotations_fpath(
            folderpath="/Users/alidzaye/rest_annotations",
            dataset="BIDS_Berlin_ECOG_LFP",
            subject=sub,
            session=session,
            task=task,
            acquisition=acquisition,
            run=run,
        )
    )
    if sub == "004":
        raw_annots = raw.set_annotations(annotations)
    else:
        raw_annots = raw.set_annotations(
            preprocessing.check_annots_orig_time(annotations)
        )
    raw_ecog = preprocessing.pick_ecog(raw_annots)
    # raw_lfp = preprocessing.pick_lfp(raw_annots)

    if sub == "012":
        raw_ecog_bi = preprocessing.bipolar_reference_s1(raw, raw_ecog, new_ch_names)
    elif sub == "010" and med == "Off":
        raw_ecog_bi = preprocessing.bipolar_reference_s10_off(
            raw, raw_ecog, new_ch_names
        )
    elif sub == "010" and med == "On":
        raw_ecog_bi = preprocessing.bipolar_reference_s10_on(
            raw, raw_ecog, new_ch_names
        )
    else:
        raw_ecog_bi = preprocessing.bipolar_reference(raw, raw_ecog, new_ch_names)

    NUM_CH = len(raw_ecog_bi.get_channel_types())

    raw_ecog_filt = preprocessing.filtering(raw_ecog_bi)

    raw_ecog_dow = preprocessing.downsample(raw_ecog_filt)

    # plot recording and save annotation
    # raw_ecog_dow.plot()
    # print("done")
    # raw_ecog_dow.annotations.save('sub-006_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_annotations.csv', overwrite=True)

    signal = preprocessing.get_data(raw_ecog_dow)

    stand_signal = preprocessing.z_score_signal(signal)

    run_TF = burst_calc.Time_Frequency_Estimation(stand_signal)

    # list of low, high, full beta bands for all channels
    if sub == "003":
        l_beta = burst_calc.beta_bands_sub3(run_TF)
    if sub == "004":
        l_beta = burst_calc.beta_bands_sub4(run_TF)
    if sub == "005":
        l_beta = burst_calc.beta_bands_sub5(run_TF)
    if sub == "006":
        l_beta = burst_calc.beta_bands_sub6(run_TF)
    if sub == "007":
        l_beta = burst_calc.beta_bands_sub7(run_TF)
    if sub == "008":
        l_beta = burst_calc.beta_bands_sub8(run_TF)
    if sub == "009":
        l_beta = burst_calc.beta_bands_sub9(run_TF)
    if sub == "010":
        l_beta = burst_calc.beta_bands_sub10(run_TF)
    if sub == "011":
        l_beta = burst_calc.beta_bands_sub11(run_TF)
    if sub == "012":
        l_beta = burst_calc.beta_bands_sub12(run_TF)
    if sub == "013":
        l_beta = burst_calc.beta_bands_sub13(run_TF)
    if sub == "014":
        l_beta = burst_calc.beta_bands_sub14(run_TF)
    if sub == "015":
        l_beta = burst_calc.beta_bands_sub15(run_TF)

    theta = 0
    mu = 1
    low = 2
    high = 3
    # full = 4
    beta = 4

    # Averaging power in all beta bands
    l_beta_avg = [burst_calc.avg_power(l) for l in l_beta]

    # Z-Scored averaged beta traces
    l_beta_avg_norm = [burst_calc.z_score(l) for l in l_beta_avg]

    # smoothing traces
    l_beta_smooth = [burst_calc.smooth(l) for l in l_beta_avg_norm[low]]

    # 75th percentile of the power
    l_beta_thr = [burst_calc.percentile(l, percentile=75) for l in l_beta_smooth]

    # Plot Signal
    # signals_array, time_array = raw_ecog_dow[:, :]
    # plt.plot(l_beta_smooth[m1], color="b")
    # plt.axhline(l_beta_thr[m1], color="r", linestyle="--")
    # sns.despine()
    # print("done")

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
        burst_calc.get_burst_length(l, l_beta_thr[idx], sfreq=250)
        for idx, l in enumerate(l_beta_smooth)
    ]
    burst_duration_cl = [
        burst_calc.exclude_short_bursts(burst_duration[ch_idx])
        for ch_idx in range(NUM_CH)
    ]
    burst_duration_cl_m1 = burst_duration_cl[m1]
    # Mean burst duration
    mean_burst_duration = [
        np.nanmean(burst_duration_cl[ch_idx], axis=0) for ch_idx in range(NUM_CH)
    ]
    mean_dur_m1 = mean_burst_duration[m1]

    # Histogram of burst duration
    histogram_duration = [
        np.histogram(burst_duration_cl[ch_idx], density=False, bins=20, range=(0, 2))[0]
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
        burst_calc.get_burst_amplitude(l, l_beta_thr[idx])
        for idx, l in enumerate(l_beta_smooth)
    ]
    burst_amplitude_m1 = burst_amplitude[m1]

    # Burst Rate
    burst_rate = [
        np.sum(histogram_duration[ch_idx] / raw_annots.times[-1])
        for ch_idx in range(len(raw_ecog_bi.get_channel_types()))
    ]
    burst_rate_m1 = burst_rate[m1]

    # 3. STRUCTURE FEATURES #
    # Burst Features
    burst_char_pd = postprocessing.dataframe_burst_char(
        mean_dur_m1, burst_amplitude_m1, burst_rate_m1
    )

    # M1 Beta Burst Dynamics
    M1_burst_dynamics = postprocessing.dataframe_burst_dynamics(normhist_dur_m1)

    # normalized beta power
    npow = postprocessing.dataframe_npow(psd_M1)

    return burst_char_pd, M1_burst_dynamics, npow
