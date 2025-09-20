import pandas as pd
import json
import requests

# Fetch CSV from IERS
url = "https://datacenter.iers.org/data/csv/bulletina.longtime.csv"
df = pd.read_csv(url)

# Filter/transform to your X,Y,Z mapping
iers_points = [
    {"x": row['X_col'], "y": row['Y_col'], "z": row['Z_col']} 
    for idx, row in df.iterrows()
]

# Load existing JSON
with open("docs/volumetric_data.json") as f:
    data = json.load(f)

# Update the IERS section
data["iers"] = iers_points

# Save updated JSON
with open("docs/volumetric_data.json", "w") as f:
    json.dump(data, f, indent=2)
