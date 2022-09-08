"""Pipelines for automated processing."""

import pathlib
import pandas as pd
import mne
from typing import Union

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
    raw_annots = raw.set_annotations(preprocessing.check_annots_orig_time(annotations))
    #raw_ecog = preprocessing.pick_ecog(raw_annots)

    if sub == '003':
        raw_lfp = preprocessing.pick_lfp3(raw_annots)
    if sub == '004':
        raw_lfp = preprocessing.pick_lfp4(raw_annots)
    if sub == '005':
        raw_lfp = preprocessing.pick_lfp5(raw_annots)
    if sub == '008':
        raw_lfp = preprocessing.pick_lfp8(raw_annots)
    if sub == '009':
        raw_lfp = preprocessing.pick_lfp9(raw_annots)
    else:
        raw_lfp = preprocessing.pick_lfp(raw_annots)

    #if sub == "012":
    #    raw_ecog_bi = preprocessing.bipolar_reference_s1(raw, raw_ecog, new_ch_names)
    #elif sub == "010" and med == "Off":
    #    raw_ecog_bi = preprocessing.bipolar_reference_s10_off(
    #        raw, raw_ecog, new_ch_names
    #    )
    #elif sub == "010" and med == "On":
    #    raw_ecog_bi = preprocessing.bipolar_reference_s10_on(
    #        raw, raw_ecog, new_ch_names
    #    )
    #else:
    #    raw_ecog_bi = preprocessing.bipolar_reference(raw, raw_ecog, new_ch_names)

    raw_lfp_bi = preprocessing.bipolar_reference_lfp(raw, raw_lfp, 'LFP_R_1_8')

    #raw_lfp_bi = raw_lfp_bi_all.ch_names[31]

    NUM_CH = len(raw_lfp_bi.ch_names)

    raw_lfp_filt = preprocessing.filtering(raw_lfp_bi)

    raw_lfp_dow = preprocessing.downsample(raw_lfp_filt)

    signal = preprocessing.get_data(raw_lfp_dow)

    #signal = signal_all[31]

    stand_signal = preprocessing.z_score_signal(signal)

    run_TF = burst_calc.Time_Frequency_Estimation(stand_signal)
    #run_TF = run_TF_all[31]

    # list of low, high, full beta bands for all channels
    l_beta = burst_calc.beta_bands(run_TF)

    # Averaging power in all beta bands
    l_beta_avg = [burst_calc.avg_power(l) for l in l_beta]

    # Z-Scored averaged beta traces
    l_beta_avg_norm = [burst_calc.z_score(l) for l in l_beta_avg]

    # 75th percentile of the power
    l_beta_thr = [burst_calc.percentile(l, percentile=75) for l in l_beta_avg_norm]

    low = 0
    high = 1
    full = 2
    mu = 3

    # 2. CALCULATING FEATURES (NORMALIZED POWER, BURST LENGTH, BURST DYNAMIC) AND BIOMARKER COMPARISON #
    # Power spectral density
    power_spectra = [
        np.nanmean(np.squeeze(run_TF[ch_idx, :, :]), axis=1)
        for ch_idx in range(len(raw_lfp_bi.get_channel_types()))
    ]
    # Normalized power spectral density
    power_spectra_norm = [
        p_ch / np.sum(p_ch[4:45] + p_ch[54:95]) for p_ch in power_spectra
    ]
    psd_lfp = power_spectra_norm[len(raw_lfp_bi.ch_names)-1]

    # Burst duration
    burst_duration = [
        burst_calc.get_burst_length(l, l_beta_thr[low][idx], sfreq=250)
        for idx, l in enumerate(l_beta_avg_norm[low])
    ]
    burst_duration_cl = [
        burst_calc.exclude_short_bursts(burst_duration[ch_idx])
        for ch_idx in range(NUM_CH)
    ]
    burst_duration_cl_lfp = burst_duration_cl[len(raw_lfp_bi.ch_names)-1]
    # Mean burst duration
    mean_burst_duration = [
        np.nanmean(burst_duration_cl[ch_idx], axis=0) for ch_idx in range(NUM_CH)
    ]
    mean_dur_lfp = mean_burst_duration[len(raw_lfp_bi.ch_names)-1]
    

    # Histogram of burst duration
    histogram_duration = [
        np.histogram(burst_duration_cl[ch_idx], density=False, bins=20, range=(0, 2))[0]
        for ch_idx in range(NUM_CH)
    ]
    hist_dur_m1 = histogram_duration[len(raw_lfp_bi.ch_names)-1]
    # Normed Histogram
    n_hist_dur = [
        100 * histogram_duration[ch_idx] / len(burst_duration_cl[ch_idx])
        for ch_idx in range(NUM_CH)
    ]
    n_hist_dur_lfp = n_hist_dur[len(raw_lfp_bi.ch_names)-1]
    n_hist_dur_lfp_cl = np.delete(n_hist_dur_lfp, 0)
    short_bursts = n_hist_dur_lfp_cl[:7]
    prol_bursts = np.sum(n_hist_dur_lfp_cl[7:])
    normhist_dur_lfp = np.append(short_bursts, prol_bursts)

    # Burst Amplitude
    burst_amplitude = [
        burst_calc.get_burst_amplitude(l, l_beta_thr[low][idx])
        for idx, l in enumerate(l_beta_avg_norm[low])
    ]
    burst_amplitude_lfp = burst_amplitude[len(raw_lfp_bi.ch_names)-1]

    # Burst Rate
    burst_rate_lfp = np.sum(histogram_duration[len(raw_lfp_bi.ch_names)-1] / raw.times[-1])

    # 3. STRUCTURE FEATURES #
    # Burst Features
    burst_char_pd = postprocessing.dataframe_burst_char(
        mean_dur_lfp, burst_amplitude_lfp, burst_rate_lfp
    )

    # M1 Beta Burst Dynamics
    M1_burst_dynamics = postprocessing.dataframe_burst_dynamics(normhist_dur_lfp)

    # normalized beta power
    npow = postprocessing.dataframe_npow(psd_lfp)

    return burst_char_pd, M1_burst_dynamics, npow
