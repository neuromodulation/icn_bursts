import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import string

ALPHA_BOX = 0.4


def plot_avgm1_burst_features(avg_features):
    sns.set(style="white", font_scale=1.5)
    fig = plt.figure(1)
    alpha_box = 0.4
    plt.subplot(131)
    sns.boxplot(
        x="Medication",
        y="Duration (s)",
        data=avg_features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 4, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Medication",
        y="Duration (s)",
        data=avg_features,
        palette="viridis",
        dodge=True,
        s=5,
    )

    plt.subplot(132)
    sns.boxplot(
        x="Medication",
        y="Amplitude (au)",
        data=avg_features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 4, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Medication",
        y="Amplitude (au)",
        data=avg_features,
        palette="viridis",
        dodge=True,
        s=5,
    )

    plt.subplot(133)
    sns.boxplot(
        x="Medication",
        y="Rate (/s)",
        data=avg_features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 4, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Medication",
        y="Rate (/s)",
        data=avg_features,
        palette="viridis",
        dodge=True,
        s=5,
    )

    # plt.suptitle("M1 burst features full beta")
    sns.despine()
    return fig


def plot_m1_burst_features(features):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(2)
    alpha_box = 0.4
    plt.subplot(311)
    sns.boxplot(
        x="Subject",
        y="Duration (s)",
        hue="Medication",
        data=features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Subject",
        y="Duration (s)",
        hue="Medication",
        data=features,
        palette="viridis",
        dodge=True,
        s=5,
    )
    plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0)
    plt.subplot(312)
    sns.boxplot(
        x="Subject",
        y="Amplitude (au)",
        hue="Medication",
        data=features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Subject",
        y="Amplitude (au)",
        hue="Medication",
        data=features,
        palette="viridis",
        dodge=True,
        s=5,
    )
    plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0)
    plt.subplot(313)
    sns.boxplot(
        x="Subject",
        y="Rate (/s)",
        hue="Medication",
        data=features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Subject",
        y="Rate (/s)",
        hue="Medication",
        data=features,
        palette="viridis",
        dodge=True,
        s=5,
    )
    plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0)
    sns.despine()
    return fig


def plot_distribution(df_gavg_dist, df_sub_dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(3)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=df_gavg_dist,
        palette="colorblind",
        saturation=0.4,
    )
    sns.stripplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=df_sub_dist,
        palette="colorblind",
        dodge=True,
        s=5,
    )
    # plt.title("Distribution of burst duration")

    sns.despine()
    return fig


def plot_gavg_psd(psd_off, psd_on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(4)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_off, label="Off")
    plt.plot(psd_on, label="On")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("averaged PSD")

    sns.despine()
    return fig


def plot_psd_s3(psd_s3off, psd_s3on):
    sns.set(style="white", font_scale=3)
    fig = plt.figure(5)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s3off, label="Off")
    plt.plot(psd_s3on, label="On")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub3")

    sns.despine()
    return fig


def plot_psd_s4(psd_s4off, psd_s4on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(6)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s4off, label="Off")
    plt.plot(psd_s4on, label="On")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub4")

    sns.despine()
    return fig


def plot_psd_s5(psd_s5off, psd_s5on_1, psd_s5on_2):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(7)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s5off, label="Off")
    plt.plot(psd_s5on_1, label="On-1")
    plt.plot(psd_s5on_2, label="On-2")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub5")

    sns.despine()
    return fig


def plot_psd_s6(psd_s6off_1, psd_s6off_2, psd_s6on_1, psd_s6on_2):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(8)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s6off_1, label="Off-1")
    plt.plot(psd_s6off_2, label="Off-2")
    plt.plot(psd_s6on_1, label="On-1")
    plt.plot(psd_s6on_2, label="On-2")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub6")

    sns.despine()
    return fig


def plot_psd_s7(psd_s7off, psd_s7on_1, psd_s7on_2):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(9)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s7off, label="Off")
    plt.plot(psd_s7on_1, label="On-1")
    plt.plot(psd_s7on_2, label="On-2")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub7")

    sns.despine()
    return fig


def plot_psd_s8(psd_s8off, psd_s8on_1, psd_s8on_2):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(10)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s8off, label="Off")
    plt.plot(psd_s8on_1, label="On-1")
    plt.plot(psd_s8on_2, label="On-2")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub8")

    sns.despine()
    return fig


def plot_psd_s9(psd_s9off_1, psd_s9off_2, psd_s9off_3, psd_s9off_4, psd_s9on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(11)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s9off_1, label="Off-1")
    plt.plot(psd_s9off_2, label="Off-2")
    plt.plot(psd_s9off_3, label="Off-3")
    plt.plot(psd_s9off_4, label="Off-4")
    plt.plot(psd_s9on, label="On")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub9")

    sns.despine()
    return fig


def plot_psd_s10(psd_s10off, psd_s10on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(12)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s10off, label="Off")
    plt.plot(psd_s10on, label="On")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub10")

    sns.despine()
    return fig


def plot_psd_s11(psd_s11off, psd_s11on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(12)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s11off, label="Off")
    plt.plot(psd_s11on, label="On")
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub11")

    sns.despine()
    return fig


def histplot_burst_length(burst_length, bins=8, range=(0.1, 0.8)):
    """ plot in histogram burst lengths"""
    sns.set(style="white", font_scale=1)
    plt.hist(burst_length, bins=bins, range=range)
    sns.despine()


def boxplot_burst_length(pd_burst_length):

    sns.boxplot(
        x="channel",
        y="value",
        hue="med_state",
        data=pd_burst_length,
        palette="viridis",
        boxprops=dict(alpha=ALPHA_BOX),
        showfliers=False,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": ALPHA_BOX},
        capprops={"alpha": ALPHA_BOX},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=ALPHA_BOX),
    )

    sns.stripplot(
        x="channel",
        y="value",
        hue="med_state",
        data=pd_burst_length,
        palette="viridis",
        dodge=True,
        s=5,
    )


def plot_betapower_vs_burstlenght(
    freqs, npow_off: list, npow_on: list, pd_burst_length: pd.DataFrame
):

    sns.set(style="white", font_scale=1.2)

    plt.figure(figsize=(25, 15))

    ax1 = plt.subplot2grid((2, 5), (0, 0), colspan=1)
    plt.yticks(np.arange(0, 0.2, step=0.05))
    ax1.set_xlabel("Frequency (Hz)")
    ax1.set_ylabel("Amplitude (au)")

    axs_col = [ax1]

    for ax_num in np.arange(1, 5):
        ax_ = plt.subplot2grid((2, 5), (0, ax_num), colspan=1)
        ax_.set_yticks(np.arange(0, 0.2, step=0.05))
        axs_col.append(ax_)

    for ch_idx, ax_ in enumerate(axs_col):
        ax_.set_ylim(0, 0.2)
        ax_.set_xlim(0, 0.2)
        ax_.plot(freqs, npow_off[ch_idx], label="MED OFF")
        ax_.plot(freqs, npow_on[ch_idx], label="MED ON")

    plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0)

    plt.subplot2grid((2, 6), (1, 0), colspan=10)

    boxplot_burst_length(pd_burst_length)

    plt.ylabel("burst duration (s)")
    plt.xlabel("")

    plt.suptitle(
        " Beta Power vs Burst Duration ECoG Berlin OFF and ON Sub003 Run01 Rest "
    )
    sns.despine()


def plot_burst_dynamics(
    freqs, npow_on, npow_off, pd_prob_dur: pd.DataFrame, pd_dur: pd.DataFrame
):

    sns.set(style="white", font_scale=1.3)
    fig, ax = plt.subplots(1, 3, figsize=(25, 15),)

    plt.subplot(131)
    plt.plot(freqs, npow_on, label="OFF ", linewidth=4)
    plt.plot(freqs, npow_off, label="ON", linewidth=4)
    plt.xlim(0, 60)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)

    plt.subplot(132)
    alpha_box = 0.3
    sns.barplot(
        data=pd_prob_dur,
        x="Burst Duration (s)",
        y="Burst Probability (%)",
        hue="Medication",
    )
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)

    plt.subplot(133)
    alpha_box = 0.4
    g = sns.boxplot(
        x="Location",
        y="Burst Duration (s)",
        hue="Medication",
        data=pd_dur,
        showfliers=False,
        meanline=dict(color="r"),
        showmeans=True,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        meanprops=dict(linestyle="-.", linewidth=5, color="r"),
    )
    plt.xlabel("Primary Motor Cortex")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)

    for n, ax in enumerate(ax):
        ax.text(
            -0.1,
            1.1,
            string.ascii_uppercase[n],
            transform=ax.transAxes,
            size=30,
            weight="bold",
        )

    sns.despine()
