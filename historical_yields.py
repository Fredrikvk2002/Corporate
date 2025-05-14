import yfinance as yf
from datetime import datetime

# === CONFIGURATION ===
ticker = "^STOXX"  # STOXX Europe 600 Index
start_date = "2020-04-01"
end_date = datetime.today().strftime('%Y-%m-%d')
risk_free_rate = 0.019  # German 3M T-bill rate

# === STEP 1: Download STOXX data ===
data = yf.download(ticker, start=start_date, end=end_date)
prices = data['Close'].dropna()

if prices.empty:
    print("Error: Could not retrieve price data.")
    exit()

# === STEP 2: Compute CAGR ===
start_price = float(prices.iloc[0])
end_price = float(prices.iloc[-1])
n_years = (prices.index[-1] - prices.index[0]).days / 365.25
cagr = (end_price / start_price) ** (1 / n_years) - 1

# === STEP 3: Compute MRP ===
mrp = cagr - risk_free_rate

# === OUTPUT ===
print(f"Start date: {prices.index[0].date()} @ {start_price:.2f}")
print(f"End date:   {prices.index[-1].date()} @ {end_price:.2f}")
print(f"Duration:   {n_years:.2f} years")
print(f"CAGR: {cagr:.2%}")
print(f"Risk-free rate: {risk_free_rate:.2%}")
print(f"Estimated Market Risk Premium: {mrp:.2%}")


