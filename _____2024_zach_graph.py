import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("detailed_for_2024_2025.csv")

df["HEIGHT_IN"] = pd.to_numeric(df["HEIGHT_IN"], errors="coerce")
df["WEIGHT"] = pd.to_numeric(df["WEIGHT"], errors="coerce")

df = df.dropna(subset=["HEIGHT_IN", "WEIGHT", "POSITION"])

plt.figure(figsize=(12, 6))

positions = df["POSITION"].unique()

for pos in positions:
    subset = df[df["POSITION"] == pos]
    plt.scatter(
        subset["WEIGHT"],
        subset["HEIGHT_IN"],
        label=pos,
        alpha=0.7,
        s=40,
        marker="o"
    )

plt.xlabel("Weight (lbs)")
plt.ylabel("Height (inches)")
plt.title("NBA 2024–25: Height vs Weight by Position")
plt.legend(title="Position")
plt.grid(True)
plt.tight_layout()


# Zach Edey
zach = df[df["PLAYER"] == "Zach Edey"].iloc[0]

plt.scatter(
    zach["WEIGHT"],
    zach["HEIGHT_IN"],
    s=80,
    edgecolors="black",
    linewidths=1.5,
    color="red"
)

plt.text(
    zach["WEIGHT"] - 6,
    zach["HEIGHT_IN"],
    "Zach Edey",
    ha="right",
    va="center",
    fontsize=10
)


plt.show()


