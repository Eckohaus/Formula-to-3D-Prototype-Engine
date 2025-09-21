import sys
import os
import pandas as pd
import requests
import json
from io import StringIO

# Add the engine folder to sys.path so we can import compute.py
sys.path.append(os.path.join(os.path.dirname(__file__)))
import compute  # now this will work both locally and in GitHub Actions

# URLs and paths
CSV_URL = "https://datacenter.iers.org/data/csv/bulletina.longtime.csv"
JSON_OUTPUT = os.path.join(os.path.dirname(__file__), "../docs/volumetric_data.json")

def fetch_and_parse_csv(url):
    """Download CSV and parse semicolon-delimited content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error downloading CSV: {e}")
        return pd.DataFrame()  # empty DataFrame on failure

    try:
        df = pd.read_csv(StringIO(response.text), sep=';', engine='python')
        return df
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
        return pd.DataFrame()

def extract_3d_points(df):
    """Extract only dX, dY, UT1-UTC columns for volumetric display."""
    required_cols = ["dX", "dY", "UT1-UTC"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Warning: Missing expected columns in CSV: {missing_cols}")
        return []

    points = [
        {"x": row["dX"], "y": row["dY"], "z": row["UT1-UTC"]}
        for _, row in df.iterrows()
        if not pd.isnull(row["dX"]) and not pd.isnull(row["dY"]) and not pd.isnull(row["UT1-UTC"])
    ]
    return points

def main():
    # Step 1: Fetch and parse CSV
    df = fetch_and_parse_csv(CSV_URL)

    # Step 2: Extract 3D points
    iers_points = extract_3d_points(df)

    # Step 3: Generate formula points using compute.py
    try:
        formula_points = compute.generate_formula_data()
    except Exception as e:
        print(f"Error generating formula points: {e}")
        formula_points = []

    # Step 4: Combine into JSON
    volumetric_data = {
        "iers": iers_points,
        "formula": formula_points
    }

    # Step 5: Save JSON to docs folder
    try:
        with open(JSON_OUTPUT, "w") as f:
            json.dump(volumetric_data, f, indent=2)
        print(f"volumetric_data.json updated: {len(iers_points)} IERS points, {len(formula_points)} formula points.")
    except Exception as e:
        print(f"Error writing JSON file: {e}")

if __name__ == "__main__":
    main()
