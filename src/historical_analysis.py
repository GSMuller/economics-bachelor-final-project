import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller
from .config import *


def calculate_volatility(series, window=30):
    """Calcula volatilidade rolling."""
    returns = series.pct_change()
    volatility = returns.rolling(window=window).std() * np.sqrt(252)
    return volatility


def structural_break_test(series, break_date):
    """Testa quebra estrutural em uma data específica."""
    pre_break = series[:break_date]
    post_break = series[break_date:]
    
    stat, pvalue = stats.levene(pre_break.dropna(), post_break.dropna())
    
    return {
        "statistic": stat,
        "p_value": pvalue,
        "pre_mean": pre_break.mean(),
        "post_mean": post_break.mean(),
        "pre_std": pre_break.std(),
        "post_std": post_break.std()
    }


def test_stationarity(series):
    """Teste Augmented Dickey-Fuller para estacionariedade."""
    result = adfuller(series.dropna())
    return {
        "adf_statistic": result[0],
        "p_value": result[1],
        "critical_values": result[4],
        "is_stationary": result[1] < 0.05
    }


def compare_periods(data, pre_period, post_period):
    """Compara estatísticas entre dois períodos."""
    pre = data[pre_period[0]:pre_period[1]]
    post = data[post_period[0]:post_period[1]]
    
    return pd.DataFrame({
        "Pre-Period": [pre.mean(), pre.std(), pre.min(), pre.max()],
        "Post-Period": [post.mean(), post.std(), post.min(), post.max()]
    }, index=["Mean", "Std Dev", "Min", "Max"])
