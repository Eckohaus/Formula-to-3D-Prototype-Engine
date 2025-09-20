import json
import numpy as np

# Example: placeholder formula data (E = mc^2)
formula_points = [
    {"x": x, "y": y, "z": x*y*0.1}  # just a simple mapping for demo
    for x in range(10)
    for y in range(10)
]

# Load IERS data if needed, or leave empty for now
iers_points = []  # Could be fetched from fetch_iers_data.py

# Combine into JSON
volumetric_data = {
    "iers": iers_points,
    "formula": formula_points
}

# Save JSON
with open("docs/volumetric_data.json", "w") as f:
    json.dump(volumetric_data, f, indent=2)
