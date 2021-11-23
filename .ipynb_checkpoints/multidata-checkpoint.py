#import libraries and modules
import mne
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as  pd
import mne_bids
import string
sns.set(style="white", font_scale=1)

#read the files with mne Bids
def read_BIDS_data(PATH_RUN, BIDS_PATH):
    """Given a run path and bids data path, read the respective data
    Parameters
    ----------
    PATH_RUN : string
    BIDS_PATH : string
    Returns
    -------
    raw_arr : mne.io.RawArray
    raw_arr_data : np.ndarray
    fs : int
    line_noise : int
    """
    entities = mne_bids.get_entities_from_fname(PATH_RUN)

    bids_path = mne_bids.BIDSPath(
        subject=entities["subject"],
        session=entities["session"],
        task=entities["task"],
        run=entities["run"],
        acquisition=entities["acquisition"],
        datatype="ieeg",
        root=BIDS_PATH,
    )

    raw_arr = mne_bids.read_raw_bids(bids_path)

    return (
        raw_arr,
        raw_arr.get_data(),
        int(np.ceil(raw_arr.info["sfreq"])),
        int(raw_arr.info["line_freq"]),
    )
PATH_BIDS = r"/Users/alidzaye/Charité - Universitätsmedizin Berlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata"
PATH_RUN = r"/Users/alidzaye/Charité - Universitätsmedizin Berlin/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EphysMedOff01/ieeg/sub-003_ses-EphysMedOff01_task-Rest_acq-StimOff_run-01_ieeg.vhdr"

raw, dat, sfreq, line_freq = read_BIDS_data(PATH_RUN, PATH_BIDS)


