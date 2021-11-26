import mne
import os
from os.path import join
from bids import BIDSLayout

# Find all StimOff Rest Files (MedOff & MedON)
def set_layout():
    '''
    Initiliaze the layout
    '''
    data_path = os.path.join('/Users/alidzaye/rawdata')
    layout = BIDSLayout(data_path)
    return layout

## Rest data OFF & ON StimOff
def find_files (layout):
    '''
    find Rest data StimOFF MedOff & MedON
    '''
    files = layout.get(extension='vhdr', task='Rest',           acquisition='StimOff', return_type='filename')
    