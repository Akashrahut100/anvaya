import numpy as np
from scipy import stats as sp_stats

def mean(data):
    return np.mean(data)

def median(data):
    return np.median(data)

def mode(data):
    return sp_stats.mode(data, keepdims=True).mode[0]

def variance(data):
    return np.var(data)

def stdev(data):
    return np.std(data)

def percentile(data, q):
    return np.percentile(data, q)

def correlation(x, y):
    return np.corrcoef(x, y)[0, 1]

def linear_regression(x, y):
    """
    Returns slope, intercept, r_value, p_value, std_err.
    """
    return sp_stats.linregress(x, y)

def describe(data):
    """
    Returns detailed descriptive statistics.
    """
    return sp_stats.describe(data)
