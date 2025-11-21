from nba_api.stats.endpoints import leaguedashplayerbiostats, commonplayerinfo
import pandas as pd
from time import sleep

print("awake")

season = "2024-25"

bio = leaguedashplayerbiostats.LeagueDashPlayerBioStats(
    season=season,
    league_id="00"
)

df = bio.get_data_frames()[0]
print("Rows:", len(df))
print("Columns:", df.columns.tolist())
print(df.head())

base = df[[
    "PLAYER_ID",
    "PLAYER_NAME",
    "TEAM_ABBREVIATION",
    "AGE",
    "PLAYER_HEIGHT",
    "PLAYER_HEIGHT_INCHES",
    "PLAYER_WEIGHT"
]].copy()

base.rename(columns={
    "PLAYER_NAME": "PLAYER",
    "TEAM_ABBREVIATION": "TEAM",
    "PLAYER_HEIGHT": "HEIGHT",
    "PLAYER_HEIGHT_INCHES": "HEIGHT_IN",
    "PLAYER_WEIGHT": "WEIGHT"
}, inplace=True)

positions = {}
unique_ids = base["PLAYER_ID"].unique()

print("Fetching positions for", len(unique_ids), "players...")

for pid in unique_ids:
    try:
        info = commonplayerinfo.CommonPlayerInfo(player_id=pid)
        info_df = info.get_data_frames()[0]
        pos = info_df.loc[0, "POSITION"]
    except Exception as e:
        print(f"Failed to get position for PLAYER_ID {pid}: {e}")
        pos = None

    positions[pid] = pos

    sleep(0.3)

pos_df = pd.DataFrame(
    [{"PLAYER_ID": pid, "POSITION": pos} for pid, pos in positions.items()]
)

full = base.merge(pos_df, on="PLAYER_ID", how="left")

full.to_csv("2024_detailed.csv", index=False)

print("Saved 2024_detailed.csv with", len(full), "rows")
print(full.head())
