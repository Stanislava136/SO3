import pandas as pd

# Load your data
df = pd.read_csv("ev-charging-station.csv")

# Ensure the columns are strings for filtering
df["ZIP"] = df["ZIP"].astype(str)
df["Country"] = df["Country"].astype(str)

# Filter for Yukon (Canadian postal codes starting with 'Y' and country == 'CA')
is_yukon = df["Country"].str.upper().eq("CA") & df["ZIP"].str.upper().str.startswith("Y")

# Count the chargers in Yukon
yukon_count = is_yukon.sum()

print(f"Number of chargers in Yukon: {yukon_count}")
