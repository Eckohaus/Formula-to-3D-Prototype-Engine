import requests
import pandas as pd
import json
from io import StringIO

# URL of IERS CSV (replace with the latest if needed)
CSV_URL = "https://datacenter.iers.org/data/csv/bulletina.longtime.csv"

try:
    # 1. Download the CSV
    response = requests.get(CSV_URL)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error downloading CSV: {e}")
    exit(1)

try:
    # 2. Read CSV into pandas DataFrame
    csv_text = response.text
    df = pd.read_csv(StringIO(csv_text), sep=";")
except Exception as e:
    print(f"Error parsing CSV: {e}")
    exit(1)

# 3. Filter the columns for volumetric display
# Make sure these match the column headers in the CSV exactly
required_columns = ["dX", "dY", "UT1-UTC"]
for col in required_columns:
    if col not in df.columns:
        print(f"Column '{col}' not found in CSV!")
        exit(1)

iers_data = [
    {"x": row["dX"], "y": row["dY"], "z": row["UT1-UTC"]}
    for _, row in df.iterrows()
]

# 4. Placeholder formula data (can be replaced with compute.py results later)
formula_data = [
    {"x": 0, "y": 0, "z": 0},
    {"x": 1, "y": 1, "z": 1}
]

# 5. Combine into JSON structure
volumetric_json = {
    "iers": iers_data,
    "formula": formula_data
}

# 6. Write JSON to the docs folder
json_file_path = "docs/volumetric_data.json"
try:
    with open(json_file_path, "w") as f:
        json.dump(volumetric_json, f, indent=2)
    print(f"Volumetric JSON updated successfully at '{json_file_path}'!")
except Exception as e:
    print(f"Error writing JSON: {e}")
    exit(1)
