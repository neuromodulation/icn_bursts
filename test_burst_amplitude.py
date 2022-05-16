"""Module for testing burst_calc.py"""
from pathlib import Path
import sys

import numpy as np

_SRC_PATH = str(Path(__file__).parent.parent / "src")
sys.path.insert(0, _SRC_PATH)

from src import burst_amplitude


