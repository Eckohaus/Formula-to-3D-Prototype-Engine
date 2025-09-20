import pandas as pd
import requests
import json

# URL of the IERS CSV (or JSON if available)
url = "https://datacenter.iers.org/data/csv/bulletina.longtime.csv"

# Fetch CSV from IERS
response = requests.get(url)
response.raise_for_status()

# Read into pandas DataFrame
from io import StringIO
df = pd.read_csv(StringIO(response.text))

# Filter / map columns for x, y, z
# Adjust column names depending on CSV
volumetric_data = []
for _, row in df.iterrows():
    volumetric_data.append({
        "x": row.get("dX", 0),
        "y": row.get("dY", 0),
        "z": row.get("UT1_UTC", 0)
    })

# Save filtered JSON to docs folder
with open("docs/volumetric_data.json", "w") as f:
    json.dump(volumetric_data, f)
