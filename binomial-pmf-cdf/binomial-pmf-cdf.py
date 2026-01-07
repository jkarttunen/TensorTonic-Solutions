import numpy as np
from scipy.special import comb

def compute_pmf(n, p, k):
    return comb(n,k) * (p ** k) * (1 - p) ** (n-k)

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = compute_pmf(n, p, k)
    cdf = 0.
    for i in range(k+1):
        cdf = cdf + compute_pmf(n, p, i)
    return (pmf, cdf)
    pass