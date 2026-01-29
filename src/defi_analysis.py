import pandas as pd
import numpy as np
from .config import *


def calculate_market_cap(price, supply):
    """Calcula capitalização de mercado."""
    return price * supply


def analyze_stablecoin_peg(stablecoin_prices, target=1.0):
    """Analisa desvio de stablecoins do peg."""
    deviation = stablecoin_prices - target
    metrics = {
        "mean_deviation": deviation.mean(),
        "std_deviation": deviation.std(),
        "max_deviation": deviation.abs().max(),
        "peg_stability": (deviation.abs() < 0.01).sum() / len(deviation)
    }
    return metrics


def calculate_tvl_dominance(protocol_tvls):
    """Calcula dominância de TVL por protocolo."""
    total_tvl = protocol_tvls.sum()
    dominance = (protocol_tvls / total_tvl) * 100
    return dominance.sort_values(ascending=False)


def calculate_correlation_matrix(crypto_prices):
    """Calcula matriz de correlação entre criptomoedas."""
    returns = crypto_prices.pct_change().dropna()
    correlation = returns.corr()
    return correlation


def analyze_volatility_comparison(traditional_assets, crypto_assets):
    """Compara volatilidade entre ativos tradicionais e cripto."""
    trad_vol = traditional_assets.pct_change().std() * np.sqrt(252)
    crypto_vol = crypto_assets.pct_change().std() * np.sqrt(252)
    
    comparison = pd.DataFrame({
        "Traditional": trad_vol,
        "Crypto": crypto_vol,
        "Ratio": crypto_vol / trad_vol
    })
    return comparison
