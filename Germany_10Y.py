import pandas as pd

def get_average_german_10y_yield():
    # Load and clean CSV
    df = pd.read_csv("Germany 10-Year Bond Yield Historical Data.csv")
    df.columns = df.columns.str.strip()

    # Convert date and filter post-COVID
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    df = df[df["Date"] >= "2020-04-01"]

    # Clean the yield column (assumed to be "Price")
    df["Price"] = df["Price"].astype(str).str.replace(',', '').str.replace('%', '').astype(float)

    # Compute average
    return df["Price"].mean()

# === Run the function ===
if __name__ == "__main__":
    avg_yield = get_average_german_10y_yield()
    print(f"Avg 10-Year Yield (Apr 2020 – Today): {avg_yield:.2f}%")
