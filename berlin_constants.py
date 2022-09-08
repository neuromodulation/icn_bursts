"""This file contains project constants for burst analysis with the Berlin
ECOG-LFP dataset."""
import os
from bids import BIDSLayout

PATH_BIDS_2 = (
    r"/Users/alidzaye/Library/CloudStorage"
    r"/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin"
    r"/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP"
    r"/rawdata"
)
data_path_2 = (
    r"/Users/alidzaye/Library/CloudStorage"
    r"/OneDrive-SharedLibraries-Charité-UniversitätsmedizinBerlin"
    r"/Interventional Cognitive Neuromodulation - Data/BIDS_Berlin_ECOG_LFP"
    r"/rawdata"
)

PATH_BIDS = (
    r"/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata"
) 

data_path = (
    r"/Users/alidzaye/BIDS_Berlin_ECOG_LFP/rawdata"
)

M1_IDS = {
    "003": 3,
    "004": 4,
    "005": 4,
    "006": 2,
    "007": 3,
    "008": 4,
    "009": 2,
    "010": 3,
    "011": 2,
    "012": 0,
    "013": 3,
    "014": 4,
}
NEW_CH_NAMES_MAP = {
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
        "ECOG_R_1_2_SMC_AT",
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT",
        "ECOG_R_5_6_SMC_AT",
    ],
    "006": [
        "ECOG_R_1_2_SMC_AT",
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT",
        "ECOG_R_5_6_SMC_AT",
    ],
    "007": [
        "ECOG_R_1_2_SMC_AT",
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT",
        "ECOG_R_5_6_SMC_AT",
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
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT",
        "ECOG_R_5_6_SMC_AT",
    ],
    "011": [
        "ECOG_R_1_2_SMC_AT",
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT",
        "ECOG_R_5_6_SMC_AT",
    ],
    "012": [
        "ECOG_R_1_2_SMC_AT",
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT"
    ],
    "013": [
        "ECOG_R_7_8_SMC_AT",
        "ECOG_R_8_9_SMC_AT",
        "ECOG_R_9_10_SMC_AT",
        "ECOG_R_10_11_SMC_AT",
        "ECOG_R_11_12_SMC_AT"
    ],
    "014": [
        "ECOG_R_1_2_SMC_AT",
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT",
        "ECOG_R_5_6_SMC_AT"
    ],
    "015": [
        "ECOG_R_1_2_SMC_AT",
        "ECOG_R_2_3_SMC_AT",
        "ECOG_R_3_4_SMC_AT",
        "ECOG_R_4_5_SMC_AT",
        "ECOG_R_5_6_SMC_AT"
    ]
}
layout = BIDSLayout(data_path)

files = layout.get(
    extension="vhdr", task="Rest", acquisition="StimOff", return_type="filename",
)

