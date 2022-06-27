"""Module for testing burst_calc.py"""
from pathlib import Path
import sys

import numpy as np

_SRC_PATH = str(Path(__file__).parent.parent / "src")
sys.path.insert(0, _SRC_PATH)

import burst_calc


class TestGetBurstLength:
    """Class for testing get_burst_length()."""

    def test_no_bursts(self) -> None:
        """Test Case where no bursts are present in data."""
        n_samples = 1000
        sfreq = 10
        threshold = 1
        power = np.zeros((n_samples,))
        bursts_len = burst_calc.get_burst_length(
            beta_averp_norm=power, beta_thr=threshold, sfreq=sfreq,
        )
        assert bursts_len.size == 0

    def test_only_bursts(self) -> None:
        """Test case where only bursts are present in data."""
        n_samples = 1000
        sfreq = 10
        threshold = 0
        power = np.ones((n_samples,))
        bursts_len = burst_calc.get_burst_length(
            beta_averp_norm=power, beta_thr=threshold, sfreq=sfreq,
        )
        np.testing.assert_array_almost_equal(bursts_len, np.array([n_samples / sfreq]))

    def test_array_starts_with_no_bursts(self) -> None:
        burst_starts = np.array([1, 400, 700])
        burst_ends = np.array([100, 600, 1000])
        n_samples = 1000
        sfreq = 10
        threshold = 0.5
        power = np.zeros((n_samples,))
        for ind, (burst_start, burst_end) in enumerate(zip(burst_starts, burst_ends)):
            power[burst_start:burst_end] = ind + 1
        bursts_len = burst_calc.get_burst_length(
            beta_averp_norm=power, beta_thr=threshold, sfreq=sfreq,
        )
        np.testing.assert_array_almost_equal(
            bursts_len, (burst_ends - burst_starts) / sfreq
        )

    def test_array_starts_with_bursts(self) -> None:
        """Test case where only bursts are present in data."""
        burst_starts = np.array([0, 400, 700])
        burst_ends = np.array([100, 600, 1000])
        n_samples = 1000
        sfreq = 10
        threshold = 0.5
        power = np.zeros((n_samples,))
        for ind, (burst_start, burst_end) in enumerate(zip(burst_starts, burst_ends)):
            power[burst_start:burst_end] = ind + 1
        bursts_len = burst_calc.get_burst_length(
            beta_averp_norm=power, beta_thr=threshold, sfreq=sfreq,
        )
        np.testing.assert_array_almost_equal(
            bursts_len, (burst_ends - burst_starts) / sfreq
        )


def main():
    """Run this script."""
    TestClass = TestGetBurstLength()
    TestClass.test_array_starts_with_bursts()
    TestClass.test_array_starts_with_no_bursts()
    TestClass.test_no_bursts()
    TestClass.test_only_bursts()


if __name__ == "__main__":
    main()
