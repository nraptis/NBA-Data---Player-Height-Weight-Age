import pandas as pd
import glob
import matplotlib.pyplot as plt

ages = {}
heights = {}
weights = {}

files = sorted(glob.glob("*_nba_data.csv"))
print("Found files:", files)

data_poitns = 0
for f in files:
    year = int(f.split("_")[0])
    df = pd.read_csv(f)
    
    if year == int(files[0].split("_")[0]):
        print("Columns in", f, ":", df.columns.tolist())

    df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")
    df["PLAYER_HEIGHT_INCHES"] = pd.to_numeric(df["PLAYER_HEIGHT_INCHES"], errors="coerce")
    df["PLAYER_WEIGHT"] = pd.to_numeric(df["PLAYER_WEIGHT"], errors="coerce")

    df_clean = df.dropna(subset=["AGE", "PLAYER_HEIGHT_INCHES", "PLAYER_WEIGHT"])

    if df_clean.empty:
        print(f"{year}: no valid rows after cleaning, skipping")
        continue

    ages[year] = df_clean["AGE"].mean()
    heights[year] = df_clean["PLAYER_HEIGHT_INCHES"].mean()
    weights[year] = df_clean["PLAYER_WEIGHT"].mean()

    data_poitns += len(df)

print("totalz: ", data_poitns)

print("AGES:", ages)
print("HEIGHTS:", heights)
print("WEIGHTS:", weights)

years_sorted = sorted(ages.keys())

averages_df = pd.DataFrame({
    "SEASON": years_sorted,
    "AVG_AGE": [ages[y] for y in years_sorted],
    "AVG_HEIGHT_INCHES": [heights[y] for y in years_sorted],
    "AVG_WEIGHT": [weights[y] for y in years_sorted],
})

print(averages_df.head())
averages_df.to_csv("averages.csv", index=False)

plt.figure(figsize=(12, 6))

plt.plot(averages_df["SEASON"], averages_df["AVG_AGE"], label="Average Age")
plt.plot(averages_df["SEASON"], averages_df["AVG_HEIGHT_INCHES"], label="Average Height (in)")
plt.plot(averages_df["SEASON"], averages_df["AVG_WEIGHT"], label="Average Weight (lbs)")

plt.title("NBA Player Averages by Season")
plt.xlabel("Season Start Year")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()