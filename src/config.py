import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
HISTORICAL_DATA_DIR = DATA_DIR / "historical"
CONTEMPORARY_DATA_DIR = DATA_DIR / "contemporary"

FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"
REPORTS_DIR = OUTPUTS_DIR / "reports"

BRETTON_WOODS_START = 1944
BRETTON_WOODS_END = 1971
NIXON_SHOCK = 1971
DERIVATIVES_ERA_START = 1972
BITCOIN_GENESIS = 2009

MAJOR_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "CHF"]
CRYPTO_SYMBOLS = ["BTC", "ETH", "USDT", "USDC", "DAI"]

BIS_API_BASE = "https://stats.bis.org/api/v1"
DEFI_LLAMA_API = "https://api.llama.fi"
