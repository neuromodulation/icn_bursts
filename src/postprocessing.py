import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def dataframe_burst_char(mean_burst_duration_M1, burst_amplitude_M1, burst_rate_M1):
    """
    Structure feature in pandas
    """
    pdburst = pd.DataFrame(
        {
            "Duration (s)": mean_burst_duration_M1,
            "Amplitude (au)": burst_amplitude_M1,
            "Rate (/s)": burst_rate_M1,
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
    feat_5on = burst_char_pd_all[5]
    feat_6off = burst_char_pd_all[6]
    feat_6on = burst_char_pd_all[7]
    feat_7off = burst_char_pd_all[8]
    feat_7on = burst_char_pd_all[9]
    feat_8off = burst_char_pd_all[10]
    feat_8on = burst_char_pd_all[11]
    feat_9off = burst_char_pd_all[12]
    feat_9on = burst_char_pd_all[13]
    feat_11off = burst_char_pd_all[14]
    feat_11on = burst_char_pd_all[15]
    feat_12off = burst_char_pd_all[16]
    feat_12on = burst_char_pd_all[17]
    feat_13off = burst_char_pd_all[18]
    feat_13on = burst_char_pd_all[19]
    feat_14off = burst_char_pd_all[20]
    feat_14on = burst_char_pd_all[21]
    feat_15off = burst_char_pd_all[22]
    feat_15on = burst_char_pd_all[23]
    #feat_16off = burst_char_pd_all[24]
    #feat_16on = burst_char_pd_all[25]

    rfeat_3off = feat_3off.drop(columns=["Run"])
    rfeat_3on = feat_3on.drop(columns=["Run"])
    rfeat_4off = feat_4off.drop(columns=["Run"])
    rfeat_4on = feat_4on.drop(columns=["Run"])
    rfeat_5off = feat_5off.drop(columns=["Run"])
    rfeat_5on = feat_5on.drop(columns=["Run"])
    rfeat_6off = feat_6off.drop(columns=["Run"])
    rfeat_6on = feat_6on.drop(columns=["Run"])
    rfeat_7off = feat_7off.drop(columns=["Run"])
    rfeat_7on = feat_7on.drop(columns=["Run"])
    rfeat_8off = feat_8off.drop(columns=["Run"])
    rfeat_8on = feat_8on.drop(columns=["Run"])
    rfeat_9off = feat_9off.drop(columns=["Run"])
    rfeat_9on = feat_9on.drop(columns=["Run"])
    rfeat_11off = feat_11off.drop(columns=["Run"])
    rfeat_11on = feat_11on.drop(columns=["Run"])
    rfeat_12off = feat_12off.drop(columns=["Run"])
    rfeat_12on = feat_12on.drop(columns=["Run"])
    rfeat_13off = feat_13off.drop(columns=["Run"])
    rfeat_13on = feat_13on.drop(columns=["Run"])
    rfeat_14off = feat_14off.drop(columns=["Run"])
    rfeat_14on = feat_14on.drop(columns=["Run"])
    rfeat_15off = feat_15off.drop(columns=["Run"])
    rfeat_15on = feat_15on.drop(columns=["Run"])


    avg_features = pd.concat(
        [
            rfeat_3off,
            rfeat_3on,
            rfeat_4off,
            rfeat_4on,
            rfeat_5off,
            rfeat_5on,
            rfeat_6off,
            rfeat_6on,
            rfeat_7off,
            rfeat_7on,
            rfeat_8off,
            rfeat_8on,
            rfeat_9off,
            rfeat_9on,
            rfeat_11off,
            rfeat_11on,
            rfeat_12off,
            rfeat_12on,
            rfeat_13off,
            rfeat_13on,
            rfeat_14off,
            rfeat_14on,
            rfeat_15off,
            rfeat_15on,
            #rfeat_16off,
            #rfeat_16on
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
    dis_s5on = (
        M1_burst_dynamics_all[5]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s6off = (
        M1_burst_dynamics_all[6]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s6on = (
        M1_burst_dynamics_all[7]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s7off = (
        M1_burst_dynamics_all[8]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s7on = (
        M1_burst_dynamics_all[9]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s8off = (
        M1_burst_dynamics_all[10]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s8on = (
        M1_burst_dynamics_all[11]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s9off = (
        M1_burst_dynamics_all[12]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s9on = (
        M1_burst_dynamics_all[13]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s11off = (
        M1_burst_dynamics_all[14]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s11on = (
        M1_burst_dynamics_all[15]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s12off = (
        M1_burst_dynamics_all[16]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s12on = (
        M1_burst_dynamics_all[17]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s13off = (
        M1_burst_dynamics_all[18]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s13on = (
        M1_burst_dynamics_all[19]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s14off = (
         M1_burst_dynamics_all[20]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s14on = (
         M1_burst_dynamics_all[21]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s15off = (
        M1_burst_dynamics_all[22]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    dis_s15on = (
        M1_burst_dynamics_all[23]
       .drop(columns=["Subject", "Medication", "Run"])
       .to_numpy()
       .flatten()
    )
    #dis_s16off = (
    #    M1_burst_dynamics_all[24]
    #    .drop(columns=["Subject", "Medication", "Run"])
    #    .to_numpy()
    #    .flatten()
    #)
    #dis_s16on = (
    #    M1_burst_dynamics_all[25]
    #   .drop(columns=["Subject", "Medication", "Run"])
    #   .to_numpy()
    #   .flatten()
    #)
    dis_off = np.nanmean(
        [
            dis_s3off,
            dis_s4off,
            dis_s5off,
            dis_s6off,
            dis_s7off,
            dis_s8off,
            dis_s9off,
            dis_s11off,
            dis_s12off,
            dis_s13off,
            dis_s14off,
            dis_s15off,
            #dis_s16off
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
            dis_s11on,
            dis_s12on,
            dis_s13on,
            dis_s14on,
            dis_s15on,
            #dis_s16on
        ],
        axis=0,
    )
    bins = [
        "0.1 - 0.2",
        "0.2 - 0.3",
        "0.3 - 0.4",
        "0.4 - 0.5",
        "0.5 - 0.6",
        "0.6 - 0.7",
        "0.7 - 0.8",
        "> 0.8",
    ]
    d_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_off}
    d_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_on}
    dt_off = pd.DataFrame(d_off)
    dt_off.insert(1, "Medication", "OFF")
    dt_on = pd.DataFrame(d_on)
    dt_on.insert(1, "Medication", "ON")

    df_gavg_dist = pd.concat([dt_off, dt_on], ignore_index=True)

    d3_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s3off}
    d3_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s3on}
    dt3_off = pd.DataFrame(d3_off)
    dt3_off.insert(1, "Medication", "OFF")
    dt3_on = pd.DataFrame(d3_on)
    dt3_on.insert(1, "Medication", "ON")

    df3_avg_dist = pd.concat([dt3_off, dt3_on], ignore_index=True)
    df3_avg_dist.insert(1, "Subject", 3)

    d4_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s4off}
    d4_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s4on}
    dt4_off = pd.DataFrame(d4_off)
    dt4_off.insert(1, "Medication", "OFF")
    dt4_on = pd.DataFrame(d4_on)
    dt4_on.insert(1, "Medication", "ON")

    df4_avg_dist = pd.concat([dt4_off, dt4_on], ignore_index=True)
    df4_avg_dist.insert(1, "Subject", 4)

    d5_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s5off}
    d5_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s5on}
    dt5_off = pd.DataFrame(d5_off)
    dt5_off.insert(1, "Medication", "OFF")
    dt5_on = pd.DataFrame(d5_on)
    dt5_on.insert(1, "Medication", "ON")

    df5_avg_dist = pd.concat([dt5_off, dt5_on], ignore_index=True)
    df5_avg_dist.insert(1, "Subject", 5)

    d6_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s6off}
    d6_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s6on}
    dt6_off = pd.DataFrame(d6_off)
    dt6_off.insert(1, "Medication", "OFF")
    dt6_on = pd.DataFrame(d6_on)
    dt6_on.insert(1, "Medication", "ON")

    df6_avg_dist = pd.concat([dt6_off, dt6_on], ignore_index=True)
    df6_avg_dist.insert(1, "Subject", 6)

    d7_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s7off}
    d7_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s7on}
    dt7_off = pd.DataFrame(d7_off)
    dt7_off.insert(1, "Medication", "OFF")
    dt7_on = pd.DataFrame(d7_on)
    dt7_on.insert(1, "Medication", "ON")

    df7_avg_dist = pd.concat([dt7_off, dt7_on], ignore_index=True)
    df7_avg_dist.insert(1, "Subject", 7)

    d8_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s8off}
    d8_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s8on}
    dt8_off = pd.DataFrame(d8_off)
    dt8_off.insert(1, "Medication", "OFF")
    dt8_on = pd.DataFrame(d8_on)
    dt8_on.insert(1, "Medication", "ON")

    df8_avg_dist = pd.concat([dt8_off, dt8_on], ignore_index=True)
    df8_avg_dist.insert(1, "Subject", 8)

    d9_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s9off}
    d9_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s9on}
    dt9_off = pd.DataFrame(d9_off)
    dt9_off.insert(1, "Medication", "OFF")
    dt9_on = pd.DataFrame(d9_on)
    dt9_on.insert(1, "Medication", "ON")

    df9_avg_dist = pd.concat([dt9_off, dt9_on], ignore_index=True)
    df9_avg_dist.insert(1, "Subject", 9)

    d11_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s11off}
    d11_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s11on}
    dt11_off = pd.DataFrame(d11_off)
    dt11_off.insert(1, "Medication", "OFF")
    dt11_on = pd.DataFrame(d11_on)
    dt11_on.insert(1, "Medication", "ON")

    df11_avg_dist = pd.concat([dt11_off, dt11_on], ignore_index=True)
    df11_avg_dist.insert(1, "Subject", 11)

    d12_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s12off}
    d12_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s12on}
    dt12_off = pd.DataFrame(d12_off)
    dt12_off.insert(1, "Medication", "OFF")
    dt12_on = pd.DataFrame(d12_on)
    dt12_on.insert(1, "Medication", "ON")

    df12_avg_dist = pd.concat([dt12_off, dt12_on], ignore_index=True)
    df12_avg_dist.insert(1, "Subject", 12)

    d13_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s13off}
    d13_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s13on}
    dt13_off = pd.DataFrame(d13_off)
    dt13_off.insert(1, "Medication", "OFF")
    dt13_on = pd.DataFrame(d13_on)
    dt13_on.insert(1, "Medication", "ON")

    df13_avg_dist = pd.concat([dt13_off, dt13_on], ignore_index=True)
    df13_avg_dist.insert(1, "Subject", 13)

    d14_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s14off}
    d14_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s14on}
    dt14_off = pd.DataFrame(d14_off)
    dt14_off.insert(1, "Medication", "OFF")
    dt14_on = pd.DataFrame(d14_on)
    dt14_on.insert(1, "Medication", "ON")

    df14_avg_dist = pd.concat([dt14_off, dt14_on], ignore_index=True)
    df14_avg_dist.insert(1, "Subject", 14)

    d15_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s15off}
    d15_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s15on}
    dt15_off = pd.DataFrame(d15_off)
    dt15_off.insert(1, "Medication", "OFF")
    dt15_on = pd.DataFrame(d15_on)
    dt15_on.insert(1, "Medication", "ON")

    df15_avg_dist = pd.concat([dt15_off, dt15_on], ignore_index=True)
    df15_avg_dist.insert(1, "Subject", 15)

    #d16_off = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s15off}
    #d16_on = {"Burst Duration (s)": bins, "Probability of Bursts (%)": dis_s15on}
    #dt16_off = pd.DataFrame(d16_off)
    #dt16_off.insert(1, "Medication", "OFF")
    #dt16_on = pd.DataFrame(d16_on)
    #dt16_on.insert(1, "Medication", "ON")

    #df16_avg_dist = pd.concat([dt16_off, dt16_on], ignore_index=True)
    #df16_avg_dist.insert(1, "Subject", 16)

    df_sub_dist = pd.concat(
        [
            df3_avg_dist,
            df4_avg_dist,
            df5_avg_dist,
            df6_avg_dist,
            df7_avg_dist,
            df8_avg_dist,
            df9_avg_dist,
            df11_avg_dist,
            df12_avg_dist,
            df13_avg_dist,
            df14_avg_dist,
            df15_avg_dist,
            #df16_avg_dist
        ]
    )
    return df_gavg_dist, df_sub_dist


def arrange_psd(npow_list_all):
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
    psd_s5on = (
        npow_list_all[5]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s6off = (
        npow_list_all[6]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s6on = (
        npow_list_all[7]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s7off = (
        npow_list_all[8]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s7on = (
        npow_list_all[9]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s8off = (
        npow_list_all[10]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s8on = (
        npow_list_all[11]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s9off = (
        npow_list_all[12]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s9on = (
        npow_list_all[13]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s11off = (
        npow_list_all[14]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s11on = (
        npow_list_all[15]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s12off = (
        npow_list_all[16]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s12on = (
        npow_list_all[17]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s13off = (
        npow_list_all[18]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s13on = (
        npow_list_all[19]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s14off = (
        npow_list_all[20]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s14on = (
        npow_list_all[21]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s15off = (
        npow_list_all[22]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    psd_s15on = (
        npow_list_all[23]
        .drop(columns=["Subject", "Medication", "Run"])
        .to_numpy()
        .flatten()
    )
    #psd_s16off = (
    #    npow_list_all[24]
    #    .drop(columns=["Subject", "Medication", "Run"])
    #    .to_numpy()
    #    .flatten()
    #)
    #psd_s16on = (
    #    npow_list_all[25]
    #    .drop(columns=["Subject", "Medication", "Run"])
    #    .to_numpy()
    #    .flatten()
    #)
    psd_off = np.mean(
        [
            psd_s3off,
            psd_s4off,
            psd_s5off,
            psd_s6off,
            psd_s7off,
            psd_s8off,
            psd_s9off,
            psd_s11off,
            psd_s12off,
            psd_s13off,
            psd_s14off,
            psd_s15off,
           # psd_s16off
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
            psd_s11on,
            psd_s12on,
            psd_s13on,
            psd_s14on,
            psd_s15on,
         #   psd_s16on
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
        psd_s11off,
        psd_s11on,
        psd_s12off,
        psd_s12on,
        psd_s13off,
        psd_s13on,
        psd_s14off,
        psd_s14on,
        psd_s15off,
        psd_s15on,
        #psd_s16off,
        #psd_s16on,
        psd_off,
        psd_on
    )

