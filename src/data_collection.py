import requests
import pandas as pd
import yfinance as yf
from datetime import datetime
from .config import *


def fetch_bis_derivatives(start_year, end_year):
    """Coleta dados de derivativos do BIS."""
    pass


def fetch_exchange_rates(currencies, start_date, end_date):
    """Coleta taxas de câmbio históricas."""
    data = {}
    for currency in currencies:
        ticker = f"{currency}=X"
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        data[currency] = df["Close"]
    return pd.DataFrame(data)


def fetch_crypto_prices(symbols, start_date, end_date):
    """Coleta preços de criptomoedas."""
    data = {}
    for symbol in symbols:
        ticker = f"{symbol}-USD"
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        data[symbol] = df["Close"]
    return pd.DataFrame(data)


def fetch_defi_tvl():
    """Coleta Total Value Locked em protocolos DeFi."""
    url = f"{DEFI_LLAMA_API}/charts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"], unit="s")
        return df
    return None


def save_data(df, filename, directory=RAW_DATA_DIR):
    """Salva dados em CSV."""
    filepath = directory / filename
    df.to_csv(filepath, index=True)
    return filepath
