import json
import os
import numpy as np

# Output folder
output_dir = "../visualization/data"
os.makedirs(output_dir, exist_ok=True)

# Placeholder formula: E = mc2
c = 3e8  # speed of light in m/s

# Example mass grid (3D 5x5x5)
mass_grid = np.linspace(1, 5, 5)
volumetric_data = []

for x in mass_grid:
    for y in mass_grid:
        for z in mass_grid:
            E = x * c**2  # simple placeholder
            volumetric_data.append({"x": x, "y": y, "z": z, "E": E})

# Save as JSON
output_file = os.path.join(output_dir, "volumetric_data.json")
with open(output_file, "w") as f:
    json.dump(volumetric_data, f, indent=2)

print(f"Volumetric data saved to {output_file}")
