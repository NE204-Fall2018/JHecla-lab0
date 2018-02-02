from __future__ import absolute_import
from code.spectrum_cal import gaus

def test_gaus_sym():
    A = 100
    B = 0
    C = 1
    xr = 2.0
    xl = -xr
    assert gaus(xr,A,B,C) == gaus(xl,A,B,C)
