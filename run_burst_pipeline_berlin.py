import runpy

import pandas as pd

from bids import BIDSLayout
import mne_bids

from src import pipelines


# SCRIPT START #
def main():
    """Run this script."""
    # Load project constants
    project_constants = runpy.run_path("project_constants.py")
    data_path = project_constants["data_path"]
    path_bids = project_constants["PATH_BIDS"]
    m1_ids = project_constants["M1_IDS"]
    new_ch_names_map = project_constants["NEW_CH_NAMES_MAP"]

    # Initialize the layout
    layout = BIDSLayout(data_path)
    files3 = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='003',
        return_type="filename",
    )
    burst_char_pd_all = []
    M1_burst_dynamics_all = []
    npow_list_all = []
    #  Process Files #
    for path_run in files3:
        entities = mne_bids.get_entities_from_fname(path_run)
        sub = entities["subject"]
        (
            burst_char_pd,
            M1_burst_dynamics,
            npow,
        ) = pipelines.bursts_single_subject(
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
    burst_char_pd_all, M1_burst_dynamics_all, npow_all = main()
    print("done")
