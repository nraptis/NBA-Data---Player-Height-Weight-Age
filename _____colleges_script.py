import glob
import pandas as pd
import matplotlib.pyplot as plt

files = sorted(glob.glob("*_nba_data.csv"))

all_rows = []

for f in files:
    try:
        year = int(f.split("_")[0])
    except:
        continue

    df = pd.read_csv(f)
    df_small = df[["PLAYER_ID", "COLLEGE"]].dropna()
    df_small["COLLEGE"] = df_small["COLLEGE"].astype(str).str.strip()

    # Accumulate
    all_rows.append(df_small)


combined = pd.concat(all_rows, ignore_index=True)

unique_players = combined.drop_duplicates(subset=["PLAYER_ID"])

college_counts = unique_players["COLLEGE"].value_counts()

top20 = college_counts.head(20)

plt.figure(figsize=(10, 6))

top20_sorted = top20.sort_values(ascending=True)  # smallest at bottom
plt.barh(top20_sorted.index, top20_sorted.values)

plt.xlabel("Unique Players (1996–2024)")
plt.ylabel("College")
plt.title("Top 20 Colleges Producing NBA Players (1996–2024)")
plt.tight_layout()
plt.show()