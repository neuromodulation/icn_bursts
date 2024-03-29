import numpy as np
import mne
from scipy import stats
import os


def remove_runs(files):
    unwanted_runs = {
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EcogLfpMedOff01/ieeg/sub-003_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EcogLfpMedOff01/ieeg/sub-003_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-3_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EcogLfpMedOn01/ieeg/sub-003_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOff01/ieeg/sub-004_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOn01/ieeg/sub-004_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOn01/ieeg/sub-004_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-3_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOn01/ieeg/sub-004_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-4_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOn02/ieeg/sub-004_ses-EcogLfpMedOn02_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-005/ses-EcogLfpMedOff01/ieeg/sub-005_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-005/ses-EcogLfpMedOff01/ieeg/sub-005_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-007/ses-EcogLfpMedOn01/ieeg/sub-007_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-007/ses-EcogLfpMedOn01/ieeg/sub-007_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-3_ieeg.vhdr",
    }
    files = [ele for ele in files if ele not in unwanted_runs]
    return files


def pick_runs(files):
    runs = {
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EcogLfpMedOff01/ieeg/sub-003_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-003/ses-EcogLfpMedOn03/ieeg/sub-003_ses-EcogLfpMedOn03_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOff01/ieeg/sub-004_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-004/ses-EcogLfpMedOn01/ieeg/sub-004_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-005/ses-EcogLfpMedOff02/ieeg/sub-005_ses-EcogLfpMedOff02_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-005/ses-EcogLfpMedOn01/ieeg/sub-005_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-006/ses-EcogLfpMedOff01/ieeg/sub-006_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-006/ses-EcogLfpMedOn01/ieeg/sub-006_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-007/ses-EcogLfpMedOff01/ieeg/sub-007_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-007/ses-EcogLfpMedOn01/ieeg/sub-007_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-2_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-008/ses-EcogLfpMedOff01/ieeg/sub-008_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-008/ses-EcogLfpMedOn01/ieeg/sub-008_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-009/ses-EcogLfpMedOff01/ieeg/sub-009_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-009/ses-EcogLfpMedOn01/ieeg/sub-009_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        #'/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-010/ses-EcogLfpMedOff01/ieeg/sub-010_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr',
        #'/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-010/ses-EcogLfpMedOn01/ieeg/sub-010_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr',
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-011/ses-EcogLfpMedOff01/ieeg/sub-011_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-011/ses-EcogLfpMedOn01/ieeg/sub-011_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-012/ses-EcogLfpMedOff02/ieeg/sub-012_ses-EcogLfpMedOff02_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-012/ses-EcogLfpMedOn01/ieeg/sub-012_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-013/ses-EcogLfpMedOff01/ieeg/sub-013_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-013/ses-EcogLfpMedOn02/ieeg/sub-013_ses-EcogLfpMedOn02_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-014/ses-EcogLfpMedOff01/ieeg/sub-014_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-014/ses-EcogLfpMedOn01/ieeg/sub-014_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-015/ses-EcogLfpMedOff01/ieeg/sub-015_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        "/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-015/ses-EcogLfpMedOn01/ieeg/sub-015_ses-EcogLfpMedOn01_task-Rest_acq-StimOff_run-1_ieeg.vhdr",
        '/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-EL016/ses-EcogLfpMedOff01/ieeg/sub-EL016_ses-EcogLfpMedOff01_task-Rest_acq-StimOff_run-1_ieeg.vhdr',
        '/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata/sub-EL016/ses-EcogLfpMedOn02/ieeg/sub-EL016_ses-EcogLfpMedOn02_task-Rest_acq-StimOff_run-1_ieeg.vhdr'
    }
    files = [i for i in files if i in runs]
    return files


def pick_ecog(raw):
    """
    pick ECoG channels
    """
    raw_ecog = []
    raw_ecog.append(raw.pick_types(ecog=True).ch_names)
    raw_ecog_red = raw_ecog[0][0:6]
    return raw_ecog_red


def pick_ecog_s13(raw):
    """
    pick ECoG channels
    """
    raw_ecog = []
    raw_ecog.append(raw.pick_types(ecog=True).ch_names)
    raw_ecog_red = raw_ecog[0][6:12]
    return raw_ecog_red


def pick_lfp(raw):
    raw_lfp = []
    raw_lfp.append(raw.pick_channels(["LFP_R_1_STN_MT", "LFP_R_8_STN_MT"]))
    return raw_lfp


def bipolar_reference(raw, raw_ecog, new_ch_names):

    anode = raw_ecog[0:5]
    cathode = raw_ecog[1:6]
    raw_ecog_bi = mne.set_bipolar_reference(
        raw.load_data(), anode=anode, cathode=cathode, ch_name=new_ch_names
    )
    return raw_ecog_bi


def bipolar_reference_s12(raw, raw_ecog, new_ch_names):

    anode = raw_ecog[0:4]
    cathode = raw_ecog[1:5]
    raw_ecog_bi = mne.set_bipolar_reference(
        raw.load_data(), anode=anode, cathode=cathode, ch_name=new_ch_names
    )
    return raw_ecog_bi


def bipolar_reference_s13(raw, raw_ecog, new_ch_names):
    anode = raw_ecog[0:5]
    cathode = raw_ecog[1:6]
    raw_new = mne.set_bipolar_reference(
        raw.load_data(), anode=anode, cathode=cathode, ch_name=new_ch_names
    )
    raw_ecog_bi = raw_new.drop_channels(
        [
            "ECOG_R_01_SMC_AT",
            "ECOG_R_02_SMC_AT",
            "ECOG_R_03_SMC_AT",
            "ECOG_R_04_SMC_AT",
            "ECOG_R_05_SMC_AT",
            "ECOG_R_06_SMC_AT",
        ]
    )
    return raw_ecog_bi


def bipolar_reference_s7_on(raw, raw_ecog, new_ch_names):
    anode = raw_ecog[0:5]
    cathode = raw_ecog[1:6]
    raw_new = mne.set_bipolar_reference(
        raw.load_data(), anode=anode, cathode=cathode, ch_name=new_ch_names
    )
    raw_ecog_bi = raw_new.drop_channels(
        [
            "ECOG_R_7_SMC_AT",
            "ECOG_R_8_SMC_AT",
            "ECOG_R_9_SMC_AT",
            "ECOG_R_10_SMC_AT",
            "ECOG_R_11_SMC_AT",
        ]
    )
    return raw_ecog_bi


def filtering(raw_ecog_bi):
    """
    Filtering (Highpass 3 Hz, Notchfilter 50,251,50Hz, Lowpass 250Hz)
    """
    raw_ecog_hi = raw_ecog_bi.filter(3, None,)
    raw_ecog_hi_lo = raw_ecog_hi.filter(None, 250)
    raw_ecog_filt = raw_ecog_hi_lo.notch_filter(
        np.arange(50, 251, 50), filter_length="auto", phase="zero"
    )
    return raw_ecog_filt


def downsample(raw_ecog_filt):
    """
    Downsample Data to 1600Hz for faster processing
    """
    raw_ecog_dow = raw_ecog_filt.resample(1600)
    return raw_ecog_dow


def get_data(raw_ecog_dow):
    signal = raw_ecog_dow.get_data(reject_by_annotation="omit")
    signal, time = raw_ecog_dow.get_data(picks=None, start=0, stop=None, reject_by_annotation='omit', return_times=True, units=None, tmin=None, tmax=raw_ecog_dow.times[-1]-5.0, verbose=None)
    return signal, time


def z_score_signal(signal):
    stand_signal = stats.zscore(signal, axis=1)
    return stand_signal


def generate_annotations_fpath(
    folderpath: str,
    dataset: str,
    subject: str,
    session: str,
    task: str,
    acquisition: str,
    run: str,
) -> str:
    """Generates a filepath for an annotations file that corresponds to an individual
    recording session based on the MNE data-storage filepath structure.
    PARAMETERS
    ----------
    folderpath : str
    -   The path of the folder where the datasets are located.
    dataset : str
    -   The name of the dataset folder within the folder given in 'folderpath'.
    subject : str
    -   The name of the subject for which the filepath should be generated.
    session : str
    -   The name of the session for which the filepath should be generated.
    task : str
    -   The name of the task for which the filepath should be generated.
    acquisition : str
    -   The name of the acquisition mode for which the filepath should be
        generated.
    run : str
    -   The name of the run for which the filepath should be generated.
    RETURNS
    -------
    str
    -   The filepath of the annotations object.
    """
    subfolders = f"{dataset}/sub-{subject}/ses-{session}"
    filename = (
        f"sub-{subject}_ses-{session}_task-{task}_acq-{acquisition}_run-{run}_"
        "annotations.csv"
    )
    return os.path.join(folderpath, subfolders, filename)


def check_annots_orig_time(annots: mne.Annotations) -> mne.Annotations:
    """Checks whether a meaningful origin time (i.e. not 1970-01-01) is present
    in the MNE Annotations object, setting it to 'None' if this is not the case.
    PARAMETERS
    ----------
    annots : MNE Annotations
    -   The annotations to check.
    RETURNS
    -------
    annots : MNE Annotations
    -   The annotations, with non-meaningful origin time corrected, if
    applicable.
    """
    orig_time = annots.orig_time
    if orig_time.day == 1 and orig_time.month == 1 and orig_time.year == 1970:
        annots = mne.Annotations(
            onset=annots.onset,
            duration=annots.duration,
            description=annots.description,
            orig_time=None,
        )
    return annots
