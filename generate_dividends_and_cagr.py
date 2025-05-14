#!/usr/bin/env python3
"""
generate_dividends_and_cagr.py

This script writes historical dividend payouts for Rheinmetall AG (RHM.DE)
to a text file and computes dividend CAGRs over different windows.
"""

import pandas as pd

# Historical dividend payouts (Date, Dividend per share)
dividend_data = [
    ("2025-05-15", 8.1),
    ("2024-05-15", 5.7),
    ("2023-05-10", 4.3),
    ("2022-05-11", 3.3),
    ("2021-05-12", 2.0),
    ("2020-05-20", 2.4),
    ("2019-05-29", 2.1),
    ("2018-05-09", 1.7),
    ("2017-05-10", 1.45),
    ("2016-05-11", 1.1),
    ("2015-05-13", 0.3),
    ("2014-05-07", 0.4),
    ("2013-05-15", 1.8),
    ("2012-05-16", 1.8),
    ("2011-05-11", 1.5),
    ("2010-05-12", 0.3),
    ("2009-05-13", 1.3),
    ("2008-05-07", 1.3),
    ("2007-05-09", 1.0),
    ("2006-05-10", 0.9),
    ("2005-05-11", 0.74),
    ("2004-05-12", 0.64),
    ("2003-05-28", 0.44),
    ("2002-06-11", 0.44),
    ("2001-06-22", 0.20),
    ("2000-06-28", 0.44)
]

# Write to a text file
txt_path = "dividends.txt"
with open(txt_path, "w") as f:
    f.write("Date,Dividend\n")
    for date, div in dividend_data:
        f.write(f"{date},{div}\n")

# Load data into DataFrame
df = pd.DataFrame(dividend_data, columns=["Date", "Dividend"])
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year

# Aggregate dividends by year
annual_div = df.groupby("Year")["Dividend"].sum().reset_index()

def compute_cagr(series, start_year, end_year):
    """
    Compute CAGR between two years inclusive.
    series: DataFrame with 'Year' and 'Dividend' columns.
    """
    start_value = series.loc[series["Year"] == start_year, "Dividend"].values[0]
    end_value = series.loc[series["Year"] == end_year, "Dividend"].values[0]
    n = end_year - start_year
    return (end_value / start_value) ** (1 / n) - 1

# Compute various CAGRs
cagr_5yr   = compute_cagr(annual_div, 2019, 2024)
cagr_10yr  = compute_cagr(annual_div, 2014, 2024)
cagr_full  = compute_cagr(annual_div, 2000, 2025)

# Display results
print(f"Dividends written to: {txt_path}")
print("\nAnnual Dividends per Year:")
print(annual_div.to_string(index=False))
print(f"\n5-year dividend CAGR (2019–2024):  {cagr_5yr:.2%}")
print(f"10-year dividend CAGR (2014–2024): {cagr_10yr:.2%}")
print(f"Full-period CAGR (2000–2024):      {cagr_full:.2%}")

