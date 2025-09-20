import pandas as pd
import requests
import json

# URL of the IERS CSV (example)
IERS_CSV_URL = "https://datacenter.iers.org/data/csv/bulletina.longtime.csv"

# Local path to save JSON (should be in docs folder for GitHub Pages)
OUTPUT_JSON_PATH = "../docs/volumetric_data.json"

# Columns to use for X, Y, Z (adjust to match your CSV)
X_COL = "X"        # e.g., dX
Y_COL = "Y"        # e.g., dY
Z_COL = "UT1-UTC"  # e.g., UT1-UTC

def fetch_csv(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise error if download fails
    return response.text

def csv_to_dataframe(csv_text):
    from io import StringIO
    df = pd.read_csv(StringIO(csv_text))
    return df

def filter_and_convert(df):
    # Ensure the columns exist
    if not all(col in df.columns for col in [X_COL, Y_COL, Z_COL]):
        raise ValueError(f"CSV missing required columns: {X_COL}, {Y_COL}, {Z_COL}")

    # Filter rows (optional, e.g., last 100 points)
    df_filtered = df.tail(100)

    # Convert to array of dicts for Plotly
    data_points = df_filtered[[X_COL, Y_COL, Z_COL]].to_dict(orient="records")
    # Rename keys to x, y, z for Plotly JS
    for point in data_points:
        point["x"] = point.pop(X_COL)
        point["y"] = point.pop(Y_COL)
        point["z"] = point.pop(Z_COL)
    return data_points

def save_json(data_points, path):
    with open(path, "w") as f:
        json.dump(data_points, f, indent=2)
    print(f"Saved {len(data_points)} points to {path}")

def main():
    csv_text = fetch_csv(IERS_CSV_URL)
    df = csv_to_dataframe(csv_text)
    data_points = filter_and_convert(df)
    save_json(data_points, OUTPUT_JSON_PATH)

if __name__ == "__main__":
    main()
