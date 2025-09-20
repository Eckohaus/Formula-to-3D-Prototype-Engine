import pandas as pd
import requests
import json

# 1. Fetch CSV from IERS
url = "https://datacenter.iers.org/data/csv/bulletina.longtime.csv"
response = requests.get(url)
response.raise_for_status()

# 2. Read into pandas
df = pd.read_csv(pd.compat.StringIO(response.text))

# 3. Filter/convert to only X, Y, Z
# Replace 'X', 'Y', 'Z' with actual column names from the dataset
points = []
for _, row in df.iterrows():
    points.append({
        "x": row["X"],
        "y": row["Y"],
        "z": row["Z"]
    })

# 4. Write JSON
with open("docs/volumetric_data.json", "w") as f:
    json.dump(points, f, indent=2)
