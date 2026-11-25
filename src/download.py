import yfinance as yf

tickers = [
    "ASML.AS", "SAP.DE", "MC.PA", "OR.PA", "AIR.PA", "SIE.DE",
    "ABI.BR", "KBC.BR", "UCB.BR", "ENEL.MI", "TTE.PA", "SAN.PA",
]

prices = yf.download(tickers, start="2019-01-01", end="2026-11-01",
                     auto_adjust=True)["Close"]

print(prices.isna().sum())
prices = prices.dropna()
prices.to_csv("data/prices.csv")
print(prices.shape)