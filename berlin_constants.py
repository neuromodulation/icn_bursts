"""This file contains project constants for burst analysis with the Berlin
ECOG-LFP dataset."""
import os
from bids import BIDSLayout

PATH_BIDS = (
    r"/Users/alidzaye/Library/CloudStorage"
    r"/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin"
    r"/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP"
    r"/rawdata"
)
data_path = (
    r"/Users/alidzaye/Library/CloudStorage"
    r"/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin"
    r"/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP"
    r"/rawdata"
)
M1_IDS = {
    "001": 2,
    "003": 3,
    "004": 4,
    "005": 4,
    "006": 2,
    "007": 3,
    "008": 4,
    "009": 2,
    "010": 4,
}
NEW_CH_NAMES_MAP = {
    "001": [
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "003": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "004": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "005": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "006": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "007": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "008": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "009": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
    "010": [
        "ECOG_L_1_2_SMC_AT",
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
}
layout = BIDSLayout(data_path)
files_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],
        return_type="filename",
    )
files1_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='001',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files1_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='003',
        session=['EcogLfpMedOn01', 'EcogLfpMedOn02', 'EcogLfpMedOn03'],
        return_type="filename",
    )
files3_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='003',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files3_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='003',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files4_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='004',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files4_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='004',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files5_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='005',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files5_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='005',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files6_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='006',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files6_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='006',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files7_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='007',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files7_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='007',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files8_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='008',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files8_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='008',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files9_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='009',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files9_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='009',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files10_off = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='010',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )
files10_on = layout.get(
        extension="vhdr",
        task="Rest",
        acquisition="StimOff",
        subject='010',
        session=['EcogLfpMedOff01','EcogLfpMedOff02', 'EcogLfpMedOff03'],
        return_type="filename",
    )