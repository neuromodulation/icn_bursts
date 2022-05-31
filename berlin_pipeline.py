from typing import Union
import runpy
from turtle import done

import pandas as pd

from bids import BIDSLayout
import mne_bids
import matplotlib.pyplot as plt
from src import pipeline


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
    remove_subjects: Union[str, None] = ["002", "010", "011", "012"]
    if remove_subjects:
        for remove_subject in remove_subjects:
            files = [file for file in files if remove_subject not in file]

    files1_off = [f for f in files if "001" in f and "MedOff" in f]
    files1_on = [f for f in files if "001" in f and "MedOn" in f]
    files3_off = [f for f in files if "003" in f and "MedOff" in f]
    files3_on = [f for f in files if "003" in f and "MedOn" in f]
    files4_off = [f for f in files if "004" in f and "MedOff" in f]
    files4_on = [f for f in files if "004" in f and "MedOn" in f]
    files5_off = [f for f in files if "005" in f and "MedOff" in f]
    files5_on = [f for f in files if "005" in f and "MedOn" in f]
    files6_off = [f for f in files if "006" in f and "MedOff" in f]
    files6_on = [f for f in files if "006" in f and "MedOn" in f]
    files7_off = [f for f in files if "007" in f and "MedOff" in f]
    files7_on = [f for f in files if "007" in f and "MedOn" in f]
    files8_off = [f for f in files if "008" in f and "MedOff" in f]
    files8_on = [f for f in files if "008" in f and "MedOn" in f]
    files9_off = [f for f in files if "009" in f and "MedOff" in f]
    files9_on = [f for f in files if "009" in f and "MedOn" in f]
    files10_off = [f for f in files if "010" in f and "MedOff" in f]
    files10_on = [f for f in files if "010" in f and "MedOn" in f]

    # Define variables
    burst_char_pd_all = []
    M1_burst_dynamics_all = []
    npow_list_all = []

    burst_char_pd_all_on = []
    M1_burst_dynamics_all_on = []
    npow_list_all_on = []

    #  Process runs in one subject #
    # def bursts_single_subject(runs):
    for path_run in files:
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
        )
        burst_char_pd["Subject"] = sub
        burst_char_pd["Medication"] = med
        burst_char_pd["Run"] = run
        M1_burst_dynamics["Subject"] = sub
        npow["Subject"] = sub
        burst_char_pd_all.append(burst_char_pd)
        M1_burst_dynamics_all.append(M1_burst_dynamics)
        npow_list_all.append(npow)

    return burst_char_pd_all, M1_burst_dynamics_all, npow_list_all


if __name__ == "__main__":
    burst_char_pd_all, M1_burst_dynamics_all, npow_list_all = main()
print(done)
