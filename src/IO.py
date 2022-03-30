import mne_bids
import numpy as np

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
        int(raw_arr.info["line_freq"]),)


