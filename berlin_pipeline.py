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
    files_3 = [f for f in files if "003" in f]
    remove_subjects: Union[str, None] = ["002", "011", "012"]
    if remove_subjects:
        for remove_subject in remove_subjects:
            files = [file for file in files if remove_subject not in file]

    # Define variables
    burst_char_pd_all = []
    M1_burst_dynamics_all = []
    npow_list_all = []

    #  Process runs in one subject #
    for path_run in files_3:
        entities = mne_bids.get_entities_from_fname(path_run)
        sub = entities["subject"]
        med = "On" if "MedOn" in entities["session"] else "Off"
        run = entities["run"]
        (burst_char_pd, M1_burst_dynamics, npow,) = pipeline.bursts_single_run(
            path_run=path_run,
            path_bids=path_bids,
            sub=sub,
            m1=m1_ids[sub],
            new_ch_names=new_ch_names_map[sub],
            med=med,
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

    return burst_char_pd_all, M1_burst_dynamics_all, npow_list_all


if __name__ == "__main__":
    burst_char_pd_all, M1_burst_dynamics_all, npow_list_all = main()


# sns.set(style="white", font_scale=1)
plt.hist(
    M1_burst_dynamics_all[0].drop(columns=["Subject", "Medication", "Run"]).to_numpy(),
    bins=np.arange(0.1, 0.9),
    range=range,
)
plt.show()


print(done)
