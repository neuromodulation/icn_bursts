from typing import Union
import runpy
from turtle import done

import pandas as pd

from bids import BIDSLayout
import mne_bids
import matplotlib.pyplot as plt
import seaborn as sns
from src import pipeline, plot_utils
import seaborn as sns
import numpy as np

# SCRIPT START #
def main():
    """Run this script."""
    # Load project constants
    project_constants = runpy.run_path("berlin_constants.py")
    data_path = project_constants["data_path"]
    path_bids = project_constants["PATH_BIDS"]
    m1_ids = project_constants["M1_IDS"]
    new_ch_names_map = project_constants["NEW_CH_NAMES_MAP"]
    files = project_constants["files"]
    files_10 = [f for f in files if "010" in f]
    remove_subjects: Union[str, None] = ["001", "002", "011", "012"]
    if remove_subjects:
        for remove_subject in remove_subjects:
            files = [file for file in files if remove_subject not in file]

    unwanted_runs = {
        "/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EcogLfpMedOff01/ieeg/sub-003_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EcogLfpMedOff01/ieeg/sub-003_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-3_ieeg.vhdr",
        "/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOff01/ieeg/sub-004_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOn01/ieeg/sub-004_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-3_ieeg.vhdr",
        "/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOn01/ieeg/sub-004_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-4_ieeg.vhdr",
        "/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-007/ses-EcogLfpMedOn01/ieeg/sub-007_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/Library/CloudStorage/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-007/ses-EcogLfpMedOn01/ieeg/sub-007_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-3_ieeg.vhdr",
    }
    files = [ele for ele in files if ele not in unwanted_runs]
    # Define variables
    burst_char_pd_all = []
    M1_burst_dynamics_all = []
    npow_list_all = []

    #  Process runs in one subject #
    for path_run in files:
        entities = mne_bids.get_entities_from_fname(path_run)
        sub = entities["subject"]
        session = entities["session"]
        task = entities["task"]
        acquisition = entities["acquisition"]
        run = entities["run"]
        med = "On" if "MedOn" in entities["session"] else "Off"
        (burst_char_pd, M1_burst_dynamics, npow,) = pipeline.bursts_single_run(
            path_run=path_run,
            path_bids=path_bids,
            sub=sub,
            m1=m1_ids[sub],
            new_ch_names=new_ch_names_map[sub],
            med=med,
            session=session,
            task=task,
            acquisition=acquisition,
            run=run,
        )
        burst_char_pd["Subject"] = sub
        burst_char_pd["Medication"] = med
        burst_char_pd["Run"] = run
        M1_burst_dynamics["Subject"] = sub
        M1_burst_dynamics["Medication"] = med
        M1_burst_dynamics["Run"] = run
        npow["Subject"] = sub
        npow["Medication"] = med
        npow["Run"] = run
        burst_char_pd_all.append(burst_char_pd)
        M1_burst_dynamics_all.append(M1_burst_dynamics)
        npow_list_all.append(npow)

    # Structure Results
    features = pd.concat(burst_char_pd_all)
    dist = pd.concat(M1_burst_dynamics_all)
    psd = pd.concat(npow_list_all)

    # Average runs for every subject
    feat_3off = burst_char_pd_all[0]
    dur_3on = np.mean([burst_char_pd_all[1].iat[0, 0], burst_char_pd_all[2].iat[0, 0]])
    feat_4off = burst_char_pd_all[3]
    dur_4on = np.mean(
        [
            burst_char_pd_all[4].iat[0, 0],
            burst_char_pd_all[5].iat[0, 0],
            burst_char_pd_all[6].iat[0, 0],
        ]
    )
    dur_5off = np.mean(
        [
            burst_char_pd_all[7].iat[0, 0],
            burst_char_pd_all[8].iat[0, 0],
            burst_char_pd_all[9].iat[0, 0],
        ]
    )
    dur_5on = np.mean(
        [burst_char_pd_all[10].iat[0, 0], burst_char_pd_all[11].iat[0, 0]]
    )
    dur_6off = np.mean(
        [burst_char_pd_all[12].iat[0, 0], burst_char_pd_all[13].iat[0, 0]]
    )
    dur_6on = np.mean(
        [burst_char_pd_all[14].iat[0, 0], burst_char_pd_all[15].iat[0, 0]]
    )
    feat_7off = burst_char_pd_all[16]
    dur_7on = np.mean(
        [burst_char_pd_all[17].iat[0, 0], burst_char_pd_all[18].iat[0, 0],]
    )
    feat_8off = burst_char_pd_all[19]
    dur_8on = np.mean(
        [burst_char_pd_all[20].iat[0, 0], burst_char_pd_all[21].iat[0, 0]]
    )
    dur_9off = np.mean(
        [
            burst_char_pd_all[22].iat[0, 0],
            burst_char_pd_all[23].iat[0, 0],
            burst_char_pd_all[24].iat[0, 0],
            burst_char_pd_all[25].iat[0, 0],
        ]
    )
    feat_9on = burst_char_pd_all[26]
    feat_10off = burst_char_pd_all[27]
    feat_10on = burst_char_pd_all[28]
    amp_3on = np.mean([burst_char_pd_all[1].iat[0, 1], burst_char_pd_all[2].iat[0, 1]])
    amp_4on = np.mean(
        [
            burst_char_pd_all[4].iat[0, 1],
            burst_char_pd_all[5].iat[0, 1],
            burst_char_pd_all[6].iat[0, 1],
        ]
    )
    amp_5off = np.mean(
        [
            burst_char_pd_all[7].iat[0, 1],
            burst_char_pd_all[8].iat[0, 1],
            burst_char_pd_all[9].iat[0, 1],
        ]
    )
    amp_5on = np.mean(
        [burst_char_pd_all[10].iat[0, 1], burst_char_pd_all[11].iat[0, 1]]
    )
    amp_6off = np.mean(
        [burst_char_pd_all[12].iat[0, 1], burst_char_pd_all[13].iat[0, 1]]
    )
    amp_6on = np.mean(
        [burst_char_pd_all[14].iat[0, 1], burst_char_pd_all[15].iat[0, 1]]
    )
    amp_7on = np.mean(
        [burst_char_pd_all[17].iat[0, 1], burst_char_pd_all[18].iat[0, 1],]
    )
    amp_8on = np.mean(
        [burst_char_pd_all[10].iat[0, 1], burst_char_pd_all[21].iat[0, 1]]
    )
    amp_9off = np.mean(
        [
            burst_char_pd_all[22].iat[0, 1],
            burst_char_pd_all[23].iat[0, 1],
            burst_char_pd_all[24].iat[0, 1],
            burst_char_pd_all[25].iat[0, 1],
        ]
    )
    rate_3on = np.mean([burst_char_pd_all[1].iat[0, 2], burst_char_pd_all[2].iat[0, 2]])
    rate_4on = np.mean(
        [
            burst_char_pd_all[4].iat[0, 2],
            burst_char_pd_all[5].iat[0, 2],
            burst_char_pd_all[6].iat[0, 2],
        ]
    )
    rate_5off = np.mean(
        [
            burst_char_pd_all[7].iat[0, 2],
            burst_char_pd_all[8].iat[0, 2],
            burst_char_pd_all[9].iat[0, 2],
        ]
    )
    rate_5on = np.mean(
        [burst_char_pd_all[10].iat[0, 2], burst_char_pd_all[11].iat[0, 2]]
    )

    rate_6off = np.mean(
        [burst_char_pd_all[12].iat[0, 2], burst_char_pd_all[13].iat[0, 2]]
    )
    rate_6on = np.mean(
        [burst_char_pd_all[14].iat[0, 2], burst_char_pd_all[15].iat[0, 2]]
    )
    rate_7on = np.mean(
        [burst_char_pd_all[17].iat[0, 2], burst_char_pd_all[18].iat[0, 2],]
    )
    rate_8on = np.mean(
        [burst_char_pd_all[20].iat[0, 2], burst_char_pd_all[21].iat[0, 2]]
    )
    rate_9off = np.mean(
        [
            burst_char_pd_all[22].iat[0, 2],
            burst_char_pd_all[23].iat[0, 2],
            burst_char_pd_all[24].iat[0, 2],
            burst_char_pd_all[25].iat[0, 2],
        ]
    )
    df_3on = pd.DataFrame(
        {
            "Duration": [dur_3on],
            "Amplitude": [amp_3on],
            "Rate": [rate_3on],
            "Subject": "003",
            "Medication": "On",
        }
    )
    df_4on = pd.DataFrame(
        {
            "Duration": [dur_4on],
            "Amplitude": [amp_4on],
            "Rate": [rate_4on],
            "Subject": "004",
            "Medication": "On",
        }
    )
    df_5off = pd.DataFrame(
        {
            "Duration": [dur_5off],
            "Amplitude": [amp_5off],
            "Rate": [rate_5off],
            "Subject": "005",
            "Medication": "Off",
        }
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
    rfeat_4off = feat_4off.drop(columns=["Run"])
    rfeat_7off = feat_7off.drop(columns=["Run"])
    rfeat_8off = feat_8off.drop(columns=["Run"])
    rfeat_9on = feat_9on.drop(columns=["Run"])
    rfeat_10off = feat_10off.drop(columns=["Run"])
    rfeat_10on = feat_10on.drop(columns=["Run"])

    avg_features = pd.concat(
        [
            rfeat_3off,
            df_3on,
            rfeat_4off,
            df_4on,
            df_5off,
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
    # data_pre = (
    #    M1_burst_dynamics_all[0]
    #    .drop(columns=["Subject", "Medication", "Run"])
    #    .to_numpy()
    # )

    # data = data_pre.flatten()
    # bins = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, ">0.8"]

    return (
        burst_char_pd_all,
        M1_burst_dynamics_all,
        npow_list_all,
        features,
        dist,
        psd,
        avg_features,
    )


if __name__ == "__main__":
    (
        burst_char_pd_all,
        M1_burst_dynamics_all,
        npow_list_all,
        features,
        dist,
        psd,
        avg_features,
    ) = main()


# PLOT FEATURES #

sns.set(style="white", font_scale=1)

print(done)

# Burst Features

plt.figure(1)
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
    x="Medication", y="Duration", data=avg_features, palette="viridis", dodge=True, s=5
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
    x="Medication", y="Amplitude", data=avg_features, palette="viridis", dodge=True, s=5
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


plt.figure(2)
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

print(done)


# Distribution of Duration
plt.figure(3)

sns.despine()


# PSD
plt.figure(4)

sns.despine()

