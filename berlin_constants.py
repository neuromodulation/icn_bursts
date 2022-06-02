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
    "001": 0,
    "003": 3,
    "004": 4,
    "005": 4,
    "006": 2,
    "007": 3,
    "008": 4,
    "009": 2,
    "010": 3,
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
        "ECOG_L_2_3_SMC_AT",
        "ECOG_L_3_4_SMC_AT",
        "ECOG_L_4_5_SMC_AT",
        "ECOG_L_5_6_SMC_AT",
    ],
}
layout = BIDSLayout(data_path)
files = layout.get(
    extension="vhdr", task="Rest", acquisition="StimOff", return_type="filename",
)

