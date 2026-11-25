# Markowitz Portfolio Optimization on European Stocks

Advanced Math project, Vrije Universiteit Brussel.

**Website:** (điền URL GitHub Pages sau)

## Research question
What does an optimal Markowitz portfolio of European stocks look like,
and does it remain efficient out-of-sample compared with an equal-weight (1/N) portfolio?

## Data
- 12 euro-denominated European stocks across sectors (ASML, SAP, LVMH, L'Oréal, Airbus,
  Siemens, AB InBev, KBC, UCB, Enel, TotalEnergies, Sanofi).
- Daily adjusted close prices from 2019-01-01 to 2026-11-01, downloaded with `yfinance`.
- Days with missing data for any stock are dropped.
- Reproduce with: `python src/download.py` (output: `data/prices.csv`).

## Analyses
1. Covariance matrix and eigendecomposition (PCA) of daily log returns. (đang làm)
2. Markowitz optimization: minimum-variance and maximum-Sharpe portfolios, efficient frontier. (chưa làm)
3. Out-of-sample test against 1/N. (chưa làm)

## Main findings

## Repository structure
- `data/` : price data (CSV)
- `src/` : download.py, analysis.py
- `figures/` : figures exported as PDF
- `website/` : website source files
- `requirements.txt` : Python dependencies

## How to run
    pip install -r requirements.txt
    python src/download.py
    python src/analysis.py
