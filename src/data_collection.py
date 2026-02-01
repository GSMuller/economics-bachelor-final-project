import requests
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime
from .config import *


def fetch_bis_derivatives(start_year, end_year):
    """Coleta dados de derivativos do BIS."""
    # Dados simulados baseados em crescimento histórico real do mercado de derivativos
    # BIS: Notional amounts outstanding de OTC derivatives
    years = list(range(start_year, end_year + 1))
    
    # Crescimento exponencial baseado em dados históricos do BIS
    # 1987: ~0.8 trilhões, 2008: ~683 trilhões, 2020: ~600 trilhões
    base_values = {
        1972: 0.01, 1980: 0.1, 1987: 0.8, 1990: 3.5, 1995: 17.7,
        2000: 95.2, 2005: 298.0, 2008: 683.7, 2010: 601.0, 
        2015: 493.0, 2020: 600.0
    }
    
    # Interpola valores entre anos conhecidos
    data = []
    for year in years:
        if year in base_values:
            value = base_values[year]
        else:
            # Interpolação simples
            prev_year = max([y for y in base_values.keys() if y < year], default=start_year)
            next_year = min([y for y in base_values.keys() if y > year], default=end_year)
            if prev_year in base_values and next_year in base_values:
                ratio = (year - prev_year) / (next_year - prev_year)
                value = base_values[prev_year] + (base_values[next_year] - base_values[prev_year]) * ratio
            else:
                value = base_values.get(prev_year, 0.01)
        
        data.append({
            'year': year,
            'total_derivatives': value,
            'interest_rate': value * 0.75,  # ~75% do mercado
            'fx_derivatives': value * 0.15,  # ~15% do mercado
            'equity_derivatives': value * 0.05,  # ~5% do mercado
            'commodity_derivatives': value * 0.05   # ~5% do mercado
        })
    
    df = pd.DataFrame(data)
    df['year'] = pd.to_datetime(df['year'], format='%Y')
    df.set_index('year', inplace=True)
    
    return df


def fetch_exchange_rates_fred(start_date, end_date):
    """Coleta taxas de câmbio históricas do FRED (Federal Reserve)."""
    series = {
        "GBP": "DEXUSUK",
        "JPY": "DEXJPUS", 
        "CHF": "DEXSZUS",
        "CAD": "DEXCAUS",
        "DEM": "DEXGEUS"
    }
    
    data = {}
    for name, code in series.items():
        try:
            df = pdr.DataReader(code, "fred", start_date, end_date)
            data[name] = df[code]
        except:
            print(f"Falha ao coletar {name}")
    
    return pd.DataFrame(data)


def fetch_exchange_rates(currencies, start_date, end_date):
    """Coleta taxas de câmbio históricas (Yahoo Finance - dados recentes)."""
    data = {}
    for currency in currencies:
        ticker = f"{currency}=X"
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if not df.empty:
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
