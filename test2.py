from __future__ import division
import numpy as np

def test_division_int():
    assert 2/8 == 0.25

def test_division_nparray():
    assert np.array([2])/8 == np.array([0.25])

