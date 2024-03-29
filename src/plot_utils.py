import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import string
from matplotlib.patheffects import PathPatchEffect, SimpleLineShadow, Normal
sns.set()

ALPHA_BOX = 0.4


def plot_avgm1_burst_features(avg_features):
    sns.set(style="white", font_scale=1)
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
    plt.xlim(4, 40)
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
    plt.plot(psd_s3off, label="Off (20)")
    plt.plot(psd_s3on, label="On (15 diff sess)")
    plt.xlim(4, 40)
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
    plt.plot(psd_s4off, label="Off (36)")
    plt.plot(psd_s4on, label="On (19)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub4")

    sns.despine()
    return fig


def plot_psd_s5(psd_s5off, psd_s5on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(7)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s5off, label="Off (18)")
    plt.plot(psd_s5on, label="On (12)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub5")

    sns.despine()
    return fig


def plot_psd_s6(psd_s6off, psd_s6on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(8)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s6off, label="Off (27)")
    plt.plot(psd_s6on, label="On (15)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub6")

    sns.despine()
    return fig


def plot_psd_s7(psd_s7off, psd_s7on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(9)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s7off, label="Off (32)")
    plt.plot(psd_s7on, label="On (13)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub7")

    sns.despine()
    return fig


def plot_psd_s8(psd_s8off, psd_s8on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(10)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s8off, label="Off (26)")
    plt.plot(psd_s8on, label="On (18)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub8")

    sns.despine()
    return fig


def plot_psd_s9(psd_s9off, psd_s9on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(11)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s9off, label="Off (15)")
    plt.plot(psd_s9on, label="On (7)")
    plt.xlim(4, 40)
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
    plt.plot(psd_s10off, label="Off (32)")
    plt.plot(psd_s10on, label="On (30)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub10")

    sns.despine()
    return fig


def plot_psd_s11(psd_s11off, psd_s11on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(13)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s11off, label="Off (43)")
    plt.plot(psd_s11on, label="On (35)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub11")

    sns.despine()
    return fig


def plot_psd_s12(psd_s12off, psd_s12on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(14)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s12off, label="Off (28)")
    plt.plot(psd_s12on, label="On (9 diff sess)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub12")

    sns.despine()
    return fig


def plot_psd_s13(psd_s13off, psd_s13on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(15)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s13off, label="Off (27)")
    plt.plot(psd_s13on, label="On (9)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub13")

    sns.despine()
    return fig


def plot_psd_s14(psd_s14off, psd_s14on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(16)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s14off, label="Off (35)")
    plt.plot(psd_s14on, label="On (13)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub14")

    sns.despine()
    return fig


def plot_psd_s15(psd_s15off, psd_s15on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(17)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s15off, label="Off (47)")
    plt.plot(psd_s15on, label="On (28)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub15")

    sns.despine()
    return fig

def plot_psd_s16(psd_s16off, psd_s16on):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(18)
    sns.set(style="white", font_scale=1)
    plt.plot(psd_s16off, label="Off (23)")
    plt.plot(psd_s16on, label="On (14)")
    plt.xlim(4, 40)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.legend(title="Medication", fontsize=15, title_fontsize=15)
    plt.title("PSD sub16")

    sns.despine()
    return fig


def plot_distribution_sub3(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(18)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 3")

    sns.despine()
    return fig


def plot_distribution_sub4(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(19)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 4")

    sns.despine()
    return fig


def plot_distribution_sub5(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(20)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 5")

    sns.despine()
    return fig


def plot_distribution_sub6(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(21)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 6")

    sns.despine()
    return fig


def plot_distribution_sub7(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(22)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 7")

    sns.despine()
    return fig


def plot_distribution_sub8(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(23)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 8")

    sns.despine()
    return fig


def plot_distribution_sub9(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(24)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 9")

    sns.despine()
    return fig


def plot_distribution_sub10(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(25)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 10")

    sns.despine()
    return fig


def plot_distribution_sub11(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(26)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 11")

    sns.despine()
    return fig


def plot_distribution_sub12(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(27)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 12")

    sns.despine()
    return fig


def plot_distribution_sub13(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(28)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 13")

    sns.despine()
    return fig


def plot_distribution_sub14(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(29)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 14")

    sns.despine()
    return fig


def plot_distribution_sub15(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(30)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 15")

    sns.despine()
    return fig

def plot_distribution_sub16(dist):
    sns.set(style="white", font_scale=1)
    fig = plt.figure(31)
    sns.barplot(
        x="Burst Duration (s)",
        y="Probability of Bursts (%)",
        hue="Medication",
        data=dist,
        palette="colorblind",
        saturation=0.4,
    )
    plt.title("Distribution LFP sub 16")

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


def plot_theta_peaks(peak_3_off,peak_4_off,peak_5_off,peak_6_off,peak_7_off,peak_8_off,peak_9_off,peak_11_off,peak_12_off,peak_13_off,peak_14_off,peak_15_off,peak_16_off,peak_3_on,peak_4_on,peak_5_on,peak_6_on,peak_7_on,peak_8_on,peak_9_on,peak_11_on,peak_12_on,peak_13_on,peak_14_on,peak_15_on,peak_16_on, peak_g_off, peak_g_on):

    fig = plt.figure(32)
    x_ticks = np.arange(-2,9)
    plt.subplot(1,2,1)
    plt.plot(x_ticks, peak_3_off,  label='3')
    plt.plot(x_ticks, peak_4_off, label='4')
    plt.plot(x_ticks, peak_5_off, label='5')
    plt.plot(x_ticks, peak_6_off, label='6')
    plt.plot(x_ticks, peak_7_off, label='7')
    plt.plot(x_ticks, peak_8_off, label='8')
    plt.plot(x_ticks, peak_9_off, label='9')
    plt.plot(x_ticks, peak_11_off, label='11')
    plt.plot(x_ticks, peak_12_off, label='12')
    plt.plot(x_ticks, peak_13_off, label='13')
    plt.plot(x_ticks, peak_14_off, label='14')
    plt.plot(x_ticks, peak_15_off, label='15')
    plt.plot(x_ticks, peak_16_off, label='16')
    plt.plot(x_ticks, peak_g_off, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=4),Normal()])
    plt.legend(title="Subject", frameon=False)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.suptitle('STN')
    plt.title('OFF')

    plt.subplot(1,2,2)
    plt.plot(x_ticks, peak_3_on, label='3')
    plt.plot(x_ticks, peak_4_on, label='4')
    plt.plot(x_ticks, peak_5_on, label='5')
    plt.plot(x_ticks, peak_6_on, label='6')
    plt.plot(x_ticks, peak_7_on, label='7')
    plt.plot(x_ticks, peak_8_on, label='8')
    plt.plot(x_ticks, peak_9_on, label='9')
    plt.plot(x_ticks, peak_11_on,label='11')
    plt.plot(x_ticks, peak_12_on, label='12')
    plt.plot(x_ticks, peak_13_on, label='13')
    plt.plot(x_ticks, peak_14_on, label='14')
    plt.plot(x_ticks, peak_15_on, label='15')
    plt.plot(x_ticks, peak_16_on, label='16')
    plt.plot(x_ticks, peak_g_on, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=4),Normal()])
    plt.legend(title="Theta", frameon=False)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.suptitle('STN')
    plt.title('ON')

    plt.show()
    return fig

def plot_beta_peaks(peak_3_off,peak_4_off,peak_5_off,peak_6_off,peak_7_off,peak_8_off,peak_9_off,peak_11_off,peak_12_off,peak_13_off,peak_14_off,peak_15_off,peak_16_off,peak_3_on,peak_4_on,peak_5_on,peak_6_on,peak_7_on,peak_8_on,peak_9_on,peak_11_on,peak_12_on,peak_13_on,peak_14_on,peak_15_on,peak_16_on, peak_g_off, peak_g_on):

    fig = plt.figure(33)
    x_ticks = np.arange(-5,6)
    plt.subplot(1,2,1)
    plt.plot(x_ticks, peak_3_off,  label='3')
    plt.plot(x_ticks, peak_4_off, label='4')
    plt.plot(x_ticks, peak_5_off, label='5')
    plt.plot(x_ticks, peak_6_off, label='6')
    plt.plot(x_ticks, peak_7_off, label='7')
    plt.plot(x_ticks, peak_8_off, label='8')
    plt.plot(x_ticks, peak_9_off, label='9')
    plt.plot(x_ticks, peak_11_off, label='11')
    plt.plot(x_ticks, peak_12_off, label='12')
    plt.plot(x_ticks, peak_13_off, label='13')
    plt.plot(x_ticks, peak_14_off, label='14')
    plt.plot(x_ticks, peak_15_off, label='15')
    plt.plot(x_ticks, peak_16_off, label='16')
    plt.plot(x_ticks, peak_g_off, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=5),Normal()])
    plt.legend(title="Beta", frameon=False)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.suptitle('STN')
    plt.title('OFF')

    plt.subplot(1,2,2)
    plt.plot(x_ticks, peak_3_on,  label='3')
    plt.plot(x_ticks, peak_4_on, label='4')
    plt.plot(x_ticks, peak_5_on, label='5')
    plt.plot(x_ticks, peak_6_on, label='6')
    plt.plot(x_ticks, peak_7_on, label='7')
    plt.plot(x_ticks, peak_8_on, label='8')
    plt.plot(x_ticks, peak_9_on, label='9')
    plt.plot(x_ticks, peak_11_on, label='11')
    plt.plot(x_ticks, peak_12_on, label='12')
    plt.plot(x_ticks, peak_13_on, label='13')
    plt.plot(x_ticks, peak_14_on, label='14')
    plt.plot(x_ticks, peak_15_on, label='15')
    plt.plot(x_ticks, peak_16_on, label='16')
    plt.plot(x_ticks, peak_g_on, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=5),Normal()])
    plt.legend(title="Beta", frameon=False)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative spectral power (au)")
    plt.suptitle('STN')
    plt.title('ON')

    return fig

def plot_duration_scores_off(duration, scores):

    plt.scatter(duration, scores)
    plt.xlabel('mean burst duration')
    plt.ylabel('UPDRS Score OFF')
    plt.title('STN full beta ')

def plot_duration_scores_on(duration, scores):

    plt.scatter(duration, scores)
    plt.xlabel('mean burst duration')
    plt.ylabel('UPDRS Score ON')
    plt.title('STN full beta ')

def plot_amplitude_scores_off(amplitude, scores):

    plt.scatter(amplitude, scores)
    plt.xlabel('mean burst amplitude')
    plt.ylabel('UPDRS Score OFF')
    plt.title('STN full beta ')

def plot_amplitude_scores_on(amplitude, scores):

    plt.scatter(amplitude, scores)
    plt.xlabel('mean burst amplitude')
    plt.ylabel('UPDRS Score ON')
    plt.title('STN full beta ')

def plot_rate_scores_off(rate, scores):

    plt.scatter(rate, scores)
    plt.xlabel('mean burst rate')
    plt.ylabel('UPDRS Score OFF')
    plt.title('STN full beta ')

def plot_rate_scores_on(rate, scores):

    plt.scatter(rate, scores)
    plt.xlabel('mean burst rate')
    plt.ylabel('UPDRS Score ON')
    plt.title('STN full beta ')


def plot_duration_scores_on(duration, scores):

    fig = plt.figure(35)
    plt.scatter(duration, scores)
    plt.xlabel('mean burst duration')
    plt.ylabel('UPDRS Score ON')
    plt.title('STN full beta ')
    return fig

def plot_amplitude_scores_off(amplitude, scores):
    
    fig = plt.figure(36)
    plt.scatter(amplitude, scores)
    plt.xlabel('mean burst amplitude')
    plt.ylabel('UPDRS Score OFF')
    plt.title('STN full beta ')
    return fig

def plot_amplitude_scores_on(amplitude, scores):

    fig = plt.figure(37)
    plt.scatter(amplitude, scores)
    plt.xlabel('mean burst amplitude')
    plt.ylabel('UPDRS Score ON')
    plt.title('STN full beta ')
    return fig

def plot_rate_scores_off(rate, scores):

    fig = plt.figure(38)
    plt.scatter(rate, scores)
    plt.xlabel('mean burst rate')
    plt.ylabel('UPDRS Score OFF')
    plt.title('STN full beta ')
    return fig

def plot_rate_scores_on(rate, scores):

    fig = plt.figure(39)
    plt.scatter(rate, scores)
    plt.xlabel('mean burst rate')
    plt.ylabel('UPDRS Score ON')
    plt.title('STN full beta ')
    return fig

def plot_duration_diff(diff, scores):

    fig = plt.figure(40)
    plt.scatter(diff, scores)
    plt.xlabel('mean burst duration')
    plt.ylabel('UPDRS Score diff')
    plt.title('STN full beta ')
    return fig

def plot_amplitude_diff(diff, scores):

    fig = plt.figure(41)
    plt.scatter(diff, scores)
    plt.xlabel('mean burst amplitude')
    plt.ylabel('UPDRS Score diff')
    plt.title('STN full beta ')
    return fig

def plot_rate_diff(diff, scores):

    fig = plt.figure(42)
    plt.scatter(diff, scores)
    plt.xlabel('mean burst rate')
    plt.ylabel('UPDRS Score diff')
    plt.title('STN full beta ')
    return fig

def plot_prol_off(diff, scores):

    fig = plt.figure(43)
    plt.scatter(diff, scores)
    plt.xlabel('prolonged bursts')
    plt.ylabel('UPDRS Score OFF')
    plt.title('STN full beta ')
    return fig

def plot_prol_on(diff, scores):

    fig = plt.figure(44)
    plt.scatter(diff, scores)
    plt.xlabel('prolonged bursts')
    plt.ylabel('UPDRS Score ON')
    plt.title('STN full beta ')
    return fig

def plot_prol_diff(diff, scores):

    fig = plt.figure(45)
    plt.scatter(diff, scores)
    plt.xlabel('prolonged bursts')
    plt.ylabel('UPDRS Score diff')
    plt.title('STN full beta ')
    return fig

def plot_dur_ampl(duration, amplitude):
    fig = plt.figure(46)
    plt.scatter(duration, amplitude)
    plt.xlabel('duration')
    plt.ylabel('Amplitude')
    plt.title('STN full beta')
    return fig


