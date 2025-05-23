import math

def norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function."""
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def black_scholes(
    S: float,
    K: float,
    t: float,
    r: float,
    sigma: float
    ) -> tuple[float, float]:
    """
    Calculate European call & put prices via Black–Scholes.
    
    Parameters
    ----------
    S     : spot price
    K     : strike price
    t     : time to expiration (years)
    r     : risk-free interest rate
    sigma : volatility (annual)
    
    Returns
    -------
    (call_price, put_price)    """
    # Compute d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - (sigma * math.sqrt(t))

    call = S * norm_cdf(d1) - K * math.exp(-r * t) * norm_cdf(d2)
    put  = K * math.exp(-r * t) * norm_cdf(-d2) - S * norm_cdf(-d1)
    return call, put