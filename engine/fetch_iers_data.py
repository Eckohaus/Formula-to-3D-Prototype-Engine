import requests
import pandas as pd
import json
from io import StringIO
from engine import compute  # assumes compute.py defines a function to generate formula data

# URL of IERS CSV
CSV_URL = "https://datacenter.iers.org/data/csv/bulletina.longtime.csv"

# --- Fetch IERS CSV ---
try:
    response = requests.get(CSV_URL)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error downloading CSV: {e}")
    exit(1)

# --- Parse CSV ---
try:
    csv_text = response.text
    df = pd.read_csv(StringIO(csv_text), sep=";")
except Exception as e:
    print(f"Error parsing CSV: {e}")
    exit(1)

# --- Filter the columns for volumetric display ---
required_columns = ["dX", "dY", "UT1-UTC"]
for col in required_columns:
    if col not in df.columns:
        print(f"Column '{col}' not found in CSV!")
        exit(1)

iers_data = [
    {"x": row["dX"], "y": row["dY"], "z": row["UT1-UTC"]}
    for _, row in df.iterrows()
]

# --- Compute formula data ---
# Make sure compute.py has a function like `generate_formula_data()`
# that returns a list of dicts: [{"x": ..., "y": ..., "z": ...}, ...]
try:
    formula_data = compute.generate_formula_data()
except Exception as e:
    print(f"Error computing formula data: {e}")
    formula_data = []

# --- Combine into JSON structure ---
volumetric_json = {
    "iers": iers_data,
    "formula": formula_data
}

# --- Write JSON to docs folder ---
json_file_path = "docs/volumetric_data.json"
try:
    with open(json_file_path, "w") as f:
        json.dump(volumetric_json, f, indent=2)
    print(f"Volumetric JSON updated successfully at '{json_file_path}'!")
except Exception as e:
    print(f"Error writing JSON: {e}")
    exit(1)
