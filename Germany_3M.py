import pandas as pd

# Load the CSV
df = pd.read_csv("Germany 3 Month Bond Yield Historical Data.csv")

# Strip column names (just in case)
df.columns = df.columns.str.strip()

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Check if Price is already float — if not, uncomment this:
# df["Price"] = df["Price"].astype(float)

# Filter post-COVID period: from April 1, 2020
df = df[df["Date"] >= "2020-04-01"]

# Compute average yield
average_yield = df["Price"].mean()

print(f"Average German 3-Month Treasury Yield (Apr 2020 – May 2025): {average_yield:.2f}%")



