# tests/test_model.py

import math
import pytest
from black_scholes.model import black_scholes

def test_black_scholes_zero_time():
    """
    When T=0, a European call is worth max(S-K, 0)
    and a put is max(K-S, 0).
    """
    S = 100.0
    K = 90.0
    T = 0.0
    r = 0.05
    sigma = 0.2

    call, put = black_scholes(S, K, T, r, sigma)
    assert pytest.approx(call, rel=1e-6) == max(S - K, 0)
    assert pytest.approx(put,  rel=1e-6) == max(K - S, 0)

def test_put_call_parity():
    """
    Check basic put–call parity:
      C - P = S - K * exp(-r*T)
    """
    S     = 100.0
    K     = 100.0
    T     = 1.0
    r     = 0.01
    sigma = 0.3

    call, put = black_scholes(S, K, T, r, sigma)
    lhs = call - put
    rhs = S - K * math.exp(-r * T)
    assert pytest.approx(lhs, rel=1e-6) == rhs