import pandas as pd

df = pd.read_csv("dataset.csv", index_col=0)  # first column is an unnamed index

# Songs per genre
print(df["track_genre"].value_counts().to_string())

# Check track_id uniqueness
dupes = df["track_id"].duplicated(keep=False)
if df["track_id"].is_unique:
    print("\nAll track_ids are unique")
else:
    print(f"\n{df['track_id'].nunique()} unique track_ids out of {len(df)} rows")
    print(df.loc[dupes, ["track_id", "track_name", "track_genre"]].sort_values("track_id"))

    #Forslag til genres swedish, acoustic, k-pop, rock, classical, disco, salsa