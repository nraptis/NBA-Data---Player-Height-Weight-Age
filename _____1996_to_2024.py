from nba_api.stats.endpoints import leaguedashplayerbiostats
import pandas as pd
import time

start_year = 1996
end_year = 2024

for year in range(start_year, end_year + 1):
    season = f"{year}-{str(year + 1)[-2:]}"   # e.g. 1996 -> "1996-97"
    print("Season:", season)

    bio = leaguedashplayerbiostats.LeagueDashPlayerBioStats(
        season=season,
        league_id="00",              # NBA
        per_mode_simple="Totals",
        season_type_all_star="Regular Season"
    )

    df = bio.get_data_frames()[0]

    if not df.empty:
        out_name = f"{year}_nba_data.csv"
        df.to_csv(out_name, index=False)
        print(f"Saved {out_name} with {len(df)} rows")
    else:
        print(f"No data for {season}, skipping.")

    time.sleep(1.0)