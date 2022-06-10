import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white", font_scale=1)


def dataframe_burst_char(mean_burst_duration_M1, burst_amplitude_M1, burst_rate_M1):
    """
    Structure feature in pandas
    """
    pdburst = pd.DataFrame(
        {
            "Duration": mean_burst_duration_M1,
            "Amplitude": burst_amplitude_M1,
            "Rate": burst_rate_M1,
        },
        index=[0],
    )
    return pdburst


def dataframe_burst_dynamics(norm_histogram_duration):
    df_probdur_M1 = pd.DataFrame(norm_histogram_duration)
    df_probdur_t_M1 = df_probdur_M1.T
    # df_his = df_probdur_t_M1.assign( Subject= 'X' , Medication = 'X', Run= 'X' )
    return df_probdur_t_M1


def dataframe_npow(power_spectra_norm):
    pw = pd.DataFrame(power_spectra_norm)
    pw_t = pw.T
    # pw_a = pw_t.assign( Subject= 'X', Medication = 'X', Run= 'X' )
    return pw_t


def average_features_sub(burst_char_pd_all):
    feat_3off = burst_char_pd_all[0]
    feat_3on = burst_char_pd_all[1]
    feat_4off = burst_char_pd_all[2]
    feat_4on = burst_char_pd_all[3]
    feat_5off = burst_char_pd_all[4]
    dur_5on = np.mean(
        [burst_char_pd_all[5].iat[0, 0], burst_char_pd_all[6].iat[0, 0]]
    )
    dur_6off = np.mean(
        [burst_char_pd_all[7].iat[0, 0], burst_char_pd_all[8].iat[0, 0]]
    )
    dur_6on = np.mean(
        [burst_char_pd_all[9].iat[0, 0], burst_char_pd_all[10].iat[0, 0]]
    )
    feat_7off = burst_char_pd_all[11]
    dur_7on = np.mean(
        [burst_char_pd_all[12].iat[0, 0], burst_char_pd_all[13].iat[0, 0],]
    )
    feat_8off = burst_char_pd_all[14]
    dur_8on = np.mean(
        [burst_char_pd_all[15].iat[0, 0], burst_char_pd_all[16].iat[0, 0]]
    )
    dur_9off = np.mean(
        [
            burst_char_pd_all[17].iat[0, 0],
            burst_char_pd_all[18].iat[0, 0],
            burst_char_pd_all[19].iat[0, 0],
            burst_char_pd_all[20].iat[0, 0],
        ]
    )
    feat_9on = burst_char_pd_all[21]
    feat_10off = burst_char_pd_all[22]
    feat_10on = burst_char_pd_all[23]
    amp_5on = np.mean(
        [burst_char_pd_all[5].iat[0, 1], burst_char_pd_all[6].iat[0, 1]]
    )
    amp_6off = np.mean(
        [burst_char_pd_all[7].iat[0, 1], burst_char_pd_all[8].iat[0, 1]]
    )
    amp_6on = np.mean(
        [burst_char_pd_all[9].iat[0, 1], burst_char_pd_all[10].iat[0, 1]]
    )
    amp_7on = np.mean(
        [burst_char_pd_all[12].iat[0, 1], burst_char_pd_all[13].iat[0, 1],]
    )
    amp_8on = np.mean(
        [burst_char_pd_all[15].iat[0, 1], burst_char_pd_all[16].iat[0, 1]]
    )
    amp_9off = np.mean(
        [
            burst_char_pd_all[17].iat[0, 1],
            burst_char_pd_all[18].iat[0, 1],
            burst_char_pd_all[19].iat[0, 1],
            burst_char_pd_all[20].iat[0, 1],
        ]
    )
    rate_5on = np.mean(
        [burst_char_pd_all[5].iat[0, 2], burst_char_pd_all[6].iat[0, 2]]
    )
    rate_6off = np.mean(
        [burst_char_pd_all[7].iat[0, 2], burst_char_pd_all[8].iat[0, 2]]
    )
    rate_6on = np.mean(
        [burst_char_pd_all[9].iat[0, 2], burst_char_pd_all[10].iat[0, 2]]
    )
    rate_7on = np.mean(
        [burst_char_pd_all[12].iat[0, 2], burst_char_pd_all[13].iat[0, 2],]
    )
    rate_8on = np.mean(
        [burst_char_pd_all[15].iat[0, 2], burst_char_pd_all[16].iat[0, 2]]
    )
    rate_9off = np.mean(
        [
            burst_char_pd_all[17].iat[0, 2],
            burst_char_pd_all[18].iat[0, 2],
            burst_char_pd_all[19].iat[0, 2],
            burst_char_pd_all[20].iat[0, 2],
        ]
    )
    df_5on = pd.DataFrame(
        {
            "Duration": [dur_5on],
            "Amplitude": [amp_5on],
            "Rate": [rate_5on],
            "Subject": "005",
            "Medication": "On",
        }
    )
    df_6off = pd.DataFrame(
        {
            "Duration": [dur_6off],
            "Amplitude": [amp_6off],
            "Rate": [rate_6off],
            "Subject": "006",
            "Medication": "Off",
        }
    )
    df_6on = pd.DataFrame(
        {
            "Duration": [dur_6on],
            "Amplitude": [amp_6on],
            "Rate": [rate_6on],
            "Subject": "006",
            "Medication": "On",
        }
    )
    df_7on = pd.DataFrame(
        {
            "Duration": [dur_7on],
            "Amplitude": [amp_7on],
            "Rate": [rate_7on],
            "Subject": "007",
            "Medication": "On",
        }
    )
    df_8on = pd.DataFrame(
        {
            "Duration": [dur_8on],
            "Amplitude": [amp_8on],
            "Rate": [rate_8on],
            "Subject": "008",
            "Medication": "On",
        }
    )
    df_9off = pd.DataFrame(
        {
            "Duration": [dur_9off],
            "Amplitude": [amp_9off],
            "Rate": [rate_9off],
            "Subject": "009",
            "Medication": "Off",
        }
    )
    rfeat_3off = feat_3off.drop(columns=["Run"])
    rfeat_3on = feat_3on.drop(columns=["Run"])
    rfeat_4off = feat_4off.drop(columns=["Run"])
    rfeat_4on = feat_4on.drop(columns=["Run"])
    rfeat_5off = feat_5off.drop(columns=["Run"])
    rfeat_7off = feat_7off.drop(columns=["Run"])
    rfeat_8off = feat_8off.drop(columns=["Run"])
    rfeat_9on = feat_9on.drop(columns=["Run"])
    rfeat_10off = feat_10off.drop(columns=["Run"])
    rfeat_10on = feat_10on.drop(columns=["Run"])

    avg_features = pd.concat(
        [
            rfeat_3off,
            rfeat_3on,
            rfeat_4off,
            rfeat_4on,
            rfeat_5off,
            df_5on,
            df_6off,
            df_6on,
            rfeat_7off,
            df_7on,
            rfeat_8off,
            df_8on,
            df_9off,
            rfeat_9on,
            rfeat_10off,
            rfeat_10on,
        ]
    )
    return avg_features


def plot_avgm1_burst_features(avg_features):
    fig = plt.figure(1)
    alpha_box = 0.4
    plt.subplot(131)
    sns.boxplot(
        x="Medication",
        y="Duration",
        data=avg_features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Medication",
        y="Duration",
        data=avg_features,
        palette="viridis",
        dodge=True,
        s=5,
    )

    plt.subplot(132)
    sns.boxplot(
        x="Medication",
        y="Amplitude",
        data=avg_features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Medication",
        y="Amplitude",
        data=avg_features,
        palette="viridis",
        dodge=True,
        s=5,
    )

    plt.subplot(133)
    sns.boxplot(
        x="Medication",
        y="Rate",
        data=avg_features,
        palette="viridis",
        boxprops=dict(alpha=alpha_box),
        showfliers=False,
        whiskerprops={"linewidth": 2, "zorder": 10, "alpha": alpha_box},
        capprops={"alpha": alpha_box},
        medianprops=dict(linestyle="-.", linewidth=5, color="grey", alpha=alpha_box),
    )
    sns.stripplot(
        x="Medication", y="Rate", data=avg_features, palette="viridis", dodge=True, s=5
    )

    plt.suptitle("M1 burst features high beta")
    sns.despine()
    return fig


def plot_m1_burst_features(features):
    fig = plt.figure(2)
    alpha_box = 0.4
    plt.subplot(311)
    sns.boxplot(
        x="Subject",
        y="Duration",
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
        y="Duration",
        hue="Medication",
        data=features,
        palette="viridis",
        dodge=True,
        s=5,
    )

    plt.subplot(312)
    sns.boxplot(
        x="Subject",
        y="Amplitude",
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
        y="Amplitude",
        hue="Medication",
        data=features,
        palette="viridis",
        dodge=True,
        s=5,
    )

    plt.subplot(313)
    sns.boxplot(
        x="Subject",
        y="Rate",
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
        y="Rate",
        hue="Medication",
        data=features,
        palette="viridis",
        dodge=True,
        s=5,
    )
    sns.despine()
    return fig
