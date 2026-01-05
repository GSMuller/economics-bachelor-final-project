# Post-1971 Monetary Regime Shift: Expectations, Volatility, and Market Behavior

This repository contains the theoretical framework and empirical analysis for an undergraduate Economics thesis on how the international monetary regime shift after 1971 (end of Bretton Woods / Nixon Shock) changed agents’ expectations, macroeconomic volatility, and financial market behavior.

---

## Research Question

**How did the post-1971 shift in the international monetary regime affect agents’ expectations and economic behavior?**

### Core Hypotheses
- **H1 — Volatility:** Macro/financial volatility increases after 1971 (e.g., FX, inflation, interest rates).
- **H2 — Expectations:** Prices become more forward-looking and sensitive to new information (higher variance, stronger regime dependence).
- **H3 — Structural Break:** Key time series display statistically significant structural breaks around 1971 (or within a short transition window).

---

## Methodological Overview

### Data (typical candidates)
- Exchange rates (USD index or major bilateral rates)
- Inflation (CPI)
- Interest rates (policy rate / long-term yields)
- Commodity prices (optional control)
- Output / unemployment (optional macro controls)

### Empirical Strategy
1. **Descriptive regime comparison** (pre vs. post 1971)
2. **Structural break tests**  
   - Chow test (known break)
   - Bai–Perron / multiple breaks (unknown breaks)
3. **Volatility modeling**  
   - Rolling volatility
   - ARCH/GARCH family (if applied)
4. **Robustness checks**  
   - Alternative break windows (e.g., 1969–1973)
   - Alternative series / countries

---

## Repository Structure

```text
.
├── data/
│   ├── raw/                # Original datasets (do not edit)
│   └── processed/          # Cleaned/merged datasets used in analysis
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_descriptive_analysis.ipynb
│   ├── 04_break_tests.ipynb
│   └── 05_volatility_models.ipynb
├── src/
│   ├── __init__.py
│   ├── config.py           # Paths, constants, break windows
│   ├── utils.py            # Helpers (io, plots, transforms)
│   ├── cleaning.py         # Data cleaning pipeline
│   ├── breaks.py           # Structural break tests
│   └── volatility.py       # Volatility estimation (rolling/GARCH)
├── outputs/
│   ├── figures/            # Charts exported from notebooks/scripts
│   └── tables/             # Regression tables, test results
├── requirements.txt
├── LICENSE
└── README.md
