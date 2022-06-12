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


def avg_features_sub(burst_char_pd_all):
    feat_3off = burst_char_pd_all[0]
    feat_3on = burst_char_pd_all[1]
    feat_4off = burst_char_pd_all[2]
    feat_4on = burst_char_pd_all[3]
    feat_5off = burst_char_pd_all[4]
    dur_5on = np.mean([burst_char_pd_all[5].iat[0, 0], burst_char_pd_all[6].iat[0, 0]])
    dur_6off = np.mean([burst_char_pd_all[7].iat[0, 0], burst_char_pd_all[8].iat[0, 0]])
    dur_6on = np.mean([burst_char_pd_all[9].iat[0, 0], burst_char_pd_all[10].iat[0, 0]])
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
    amp_5on = np.mean([burst_char_pd_all[5].iat[0, 1], burst_char_pd_all[6].iat[0, 1]])
    amp_6off = np.mean([burst_char_pd_all[7].iat[0, 1], burst_char_pd_all[8].iat[0, 1]])
    amp_6on = np.mean([burst_char_pd_all[9].iat[0, 1], burst_char_pd_all[10].iat[0, 1]])
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
    rate_5on = np.mean([burst_char_pd_all[5].iat[0, 2], burst_char_pd_all[6].iat[0, 2]])
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


def avg_distribution(M1_burst_dynamics_all):

    dis_s3off = (
        M1_burst_dynamics_all[0]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s3on = (
        M1_burst_dynamics_all[1]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s4off = (
        M1_burst_dynamics_all[2]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s4on = (
        M1_burst_dynamics_all[3]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s5off = (
        M1_burst_dynamics_all[4]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s5on = np.mean(
        np.array(
            [
                M1_burst_dynamics_all[5]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                M1_burst_dynamics_all[6]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    dis_s6off = np.mean(
        np.array(
            [
                M1_burst_dynamics_all[7]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                M1_burst_dynamics_all[8]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    dis_s6on = np.mean(
        np.array(
            [
                M1_burst_dynamics_all[9]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                M1_burst_dynamics_all[10]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    dis_s7off = (
        M1_burst_dynamics_all[11]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s7on = np.mean(
        np.array(
            [
                M1_burst_dynamics_all[12]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                M1_burst_dynamics_all[13]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    dis_s8off = (
        M1_burst_dynamics_all[14]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s8on = np.mean(
        np.array(
            [
                M1_burst_dynamics_all[15]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                M1_burst_dynamics_all[16]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    dis_s9off = np.mean(
        [
            M1_burst_dynamics_all[17]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
            M1_burst_dynamics_all[18]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
            M1_burst_dynamics_all[19]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
            M1_burst_dynamics_all[20]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
        ],
        axis=0,
    )
    dis_s9on = (
        M1_burst_dynamics_all[21]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s10off = (
        M1_burst_dynamics_all[22]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s10on = (
        M1_burst_dynamics_all[23]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_off = np.mean(
        [
            dis_s3off,
            dis_s4off,
            dis_s5off,
            dis_s6off,
            dis_s7off,
            dis_s8off,
            dis_s9off,
            dis_s10off,
        ],
        axis=0,
    )
    dis_on = np.mean(
        [
            dis_s3on,
            dis_s4on,
            dis_s5on,
            dis_s6on,
            dis_s7on,
            dis_s8on,
            dis_s9on,
            dis_s10on,
        ],
        axis=0,
    )
    bins = [
        "0.1-0.2",
        "0.2-0.3",
        "0.3-0.4",
        "0.4-0.5",
        "0.5-0.6",
        "0.6-0.7",
        "0.7-0.8",
        ">0.8",
    ]
    d_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_off}
    d_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_on}
    dt_off = pd.DataFrame(d_off)
    dt_off.insert(1, "Medication", "Off")
    dt_on = pd.DataFrame(d_on)
    dt_on.insert(1, "Medication", "On")

    df_gavg_dist = pd.concat([dt_off, dt_on], ignore_index=True)

    d3_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s3off}
    d3_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s3on}
    dt3_off = pd.DataFrame(d3_off)
    dt3_off.insert(1, "Medication", "Off")
    dt3_on = pd.DataFrame(d3_on)
    dt3_on.insert(1, "Medication", "On")

    df3_avg_dist = pd.concat([dt3_off, dt3_on], ignore_index=True)
    df3_avg_dist.insert(1, "Subject", 3)

    d4_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s4off}
    d4_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s4on}
    dt4_off = pd.DataFrame(d4_off)
    dt4_off.insert(1, "Medication", "Off")
    dt4_on = pd.DataFrame(d4_on)
    dt4_on.insert(1, "Medication", "On")

    df4_avg_dist = pd.concat([dt4_off, dt4_on], ignore_index=True)
    df4_avg_dist.insert(1, "Subject", 4)

    d5_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s5off}
    d5_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s5on}
    dt5_off = pd.DataFrame(d5_off)
    dt5_off.insert(1, "Medication", "Off")
    dt5_on = pd.DataFrame(d5_on)
    dt5_on.insert(1, "Medication", "On")

    df5_avg_dist = pd.concat([dt5_off, dt5_on], ignore_index=True)
    df5_avg_dist.insert(1, "Subject", 5)

    d6_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s6off}
    d6_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s6on}
    dt6_off = pd.DataFrame(d6_off)
    dt6_off.insert(1, "Medication", "Off")
    dt6_on = pd.DataFrame(d6_on)
    dt6_on.insert(1, "Medication", "On")

    df6_avg_dist = pd.concat([dt6_off, dt6_on], ignore_index=True)
    df6_avg_dist.insert(1, "Subject", 6)

    d7_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s7off}
    d7_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s7on}
    dt7_off = pd.DataFrame(d7_off)
    dt7_off.insert(1, "Medication", "Off")
    dt7_on = pd.DataFrame(d7_on)
    dt7_on.insert(1, "Medication", "On")

    df7_avg_dist = pd.concat([dt7_off, dt7_on], ignore_index=True)
    df7_avg_dist.insert(1, "Subject", 7)

    d8_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s8off}
    d8_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s8on}
    dt8_off = pd.DataFrame(d8_off)
    dt8_off.insert(1, "Medication", "Off")
    dt8_on = pd.DataFrame(d8_on)
    dt8_on.insert(1, "Medication", "On")

    df8_avg_dist = pd.concat([dt8_off, dt8_on], ignore_index=True)
    df8_avg_dist.insert(1, "Subject", 8)

    d9_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s9off}
    d9_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s9on}
    dt9_off = pd.DataFrame(d9_off)
    dt9_off.insert(1, "Medication", "Off")
    dt9_on = pd.DataFrame(d9_on)
    dt9_on.insert(1, "Medication", "On")

    df9_avg_dist = pd.concat([dt9_off, dt9_on], ignore_index=True)
    df9_avg_dist.insert(1, "Subject", 9)

    d10_off = {"burst duration (s)": bins, "probability of bursts (%)": dis_s10off}
    d10_on = {"burst duration (s)": bins, "probability of bursts (%)": dis_s10on}
    dt10_off = pd.DataFrame(d10_off)
    dt10_off.insert(1, "Medication", "Off")
    dt10_on = pd.DataFrame(d10_on)
    dt10_on.insert(1, "Medication", "On")

    df10_avg_dist = pd.concat([dt10_off, dt10_on], ignore_index=True)
    df10_avg_dist.insert(1, "Subject", 10)

    df_sub_dist = pd.concat(
        [
            df3_avg_dist,
            df4_avg_dist,
            df5_avg_dist,
            df6_avg_dist,
            df7_avg_dist,
            df8_avg_dist,
            df9_avg_dist,
            df10_avg_dist,
        ]
    )
    return df_gavg_dist, df_sub_dist


def avg_psd(npow_list_all):
    psd_s3off = (
        npow_list_all[0]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s3on = (
        npow_list_all[1]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s4off = (
        npow_list_all[2]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s4on = (
        npow_list_all[3]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s5off = (
        npow_list_all[4]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s5on = np.mean(
        np.array(
            [
                npow_list_all[5]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                npow_list_all[6]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    psd_s6off = np.mean(
        np.array(
            [
                npow_list_all[7]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                npow_list_all[8]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    psd_s6on = np.mean(
        np.array(
            [
                npow_list_all[9]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                npow_list_all[10]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    psd_s7off = (
        npow_list_all[11]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s7on = np.mean(
        np.array(
            [
                npow_list_all[12]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                npow_list_all[13]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    psd_s8off = (
        npow_list_all[14]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s8on = np.mean(
        np.array(
            [
                npow_list_all[15]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
                npow_list_all[16]
                .drop(columns=["Subject", "Medication", "Run"])
                .to_numpy()
                .flatten(),
            ]
        ),
        axis=0,
    )
    psd_s9off = np.mean(
        [
            npow_list_all[17]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
            npow_list_all[18]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
            npow_list_all[19]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
            npow_list_all[20]
            .drop(columns=["Subject", "Medication", "Run"])
            .to_numpy()
            .flatten(),
        ],
        axis=0,
    )
    psd_s9on = (
        npow_list_all[21]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s10off = (
        npow_list_all[22]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s10on = (
        npow_list_all[23]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_off = np.mean(
        [
            psd_s3off,
            psd_s4off,
            psd_s5off,
            psd_s6off,
            psd_s7off,
            psd_s8off,
            psd_s9off,
            psd_s10off,
        ],
        axis=0,
    )
    psd_on = np.mean(
        [
            psd_s3on,
            psd_s4on,
            psd_s5on,
            psd_s6on,
            psd_s7on,
            psd_s8on,
            psd_s9on,
            psd_s10on,
        ],
        axis=0,
    )
    return (
        psd_s3off,
        psd_s3on,
        psd_s4off,
        psd_s4on,
        psd_s5off,
        psd_s5on,
        psd_s6off,
        psd_s6on,
        psd_s7off,
        psd_s7on,
        psd_s8off,
        psd_s8on,
        psd_s9off,
        psd_s9on,
        psd_s10off,
        psd_s10on,
        psd_off,
        psd_on,
    )

