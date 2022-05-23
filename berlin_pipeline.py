import runpy

import pandas as pd

from bids import BIDSLayout
import mne_bids

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
    files_off = project_constants["files_off"]
    files_on = project_constants["files_on"]
    files1_off = project_constants["files1_off"]
    files1_on = project_constants["files1_on"]
    files3_off = project_constants["files3_off"]
    files3_on = project_constants["files3_on"]
    files4_off = project_constants["files4_off"]
    files4_on = project_constants["files4_on"]
    files5_off = project_constants["files5_off"]
    files5_on = project_constants["files5_on"]
    files6_off = project_constants["files6_off"]
    files6_on = project_constants["files6_on"]
    files7_off = project_constants["files7_off"]
    files7_on = project_constants["files7_on"]
    files8_off = project_constants["files8_off"]
    files8_on = project_constants["files8_on"]
    files9_off = project_constants["files9_off"]
    files9_on = project_constants["files9_on"]
    files10_off = project_constants["files10_off"]
    files10_on = project_constants["files10_on"]

    # Define variables
    burst_char_pd_all = []
    M1_burst_dynamics_all = []
    npow_list_all = []

    #  Process Files #
    for path_run in files3_off:
        entities = mne_bids.get_entities_from_fname(path_run)
        sub = entities["subject"]
        (
            burst_char_pd,
            M1_burst_dynamics,
            npow,
        ) = pipeline.bursts_single_subject(
            path_run=path_run,
            path_bids=path_bids,
            sub=sub,
            m1=m1_ids[sub],
            new_ch_names=new_ch_names_map[sub],
        )
        burst_char_pd["Subject"] = sub
        M1_burst_dynamics["Subject"] = sub
        npow["Subject"] = sub
        burst_char_pd_all.append(burst_char_pd)
        M1_burst_dynamics_all.append(M1_burst_dynamics)
        npow_list_all.append(npow)

#    burst_char_pd_df = pd.DataFrame(burst_char_pd_all)
#    M1_burst_dynamics_df = pd.DataFrame(M1_burst_dynamics_all)
#    npow_df = pd.DataFrame(npow_list_all)



    return burst_char_pd_all, M1_burst_dynamics_all, npow_list_all


if __name__ == "__main__":
    burst_char_pd_all, M1_burst_dynamics_all, npow_list_all = main()
    print("done")
