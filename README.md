# Formula-to-3D Prototype Engine
Prototype engine to convert physics formulas into volumetric 3D outputs.

**Description:**  This project demonstrates how physics formulas (e.g., E = mc²) and external scientific datasets can be transformed into **interactive volumetric 3D visualizations**, deployable via cloud APIs and GitHub Pages.

---

## Features
- Compute volumetric data from formulas on a 3D grid
- Fetch and process scientific datasets (currently IERS Earth orientation parameters)
- Simple REST API to trigger computation
- Interactive 3D visualization using Plotly.js
- Mobile-accessible and cloud-deployable

## Data Sources & Attribution
This project integrates external datasets for visualization:

- **IERS Earth Orientation Parameters (EOP) data**
Provided by the [International Earth Rotation and Reference Systems Service (IERS)](https://www.iers.org/IERS/EN/DataProducts/EarthOrientationData/eop.html)
The IERS is the authoritative source for Earth orientation parameters. This repository only fetches and reformats the data for visualization purposes.

If you use or redistribute this project, please also credit the IERS as the original data provider.

---

## Getting Started
1. Clone the repository to your cloud IDE (e.g., Replit, Render.com)
2. Install dependencies:
    ```bash
    pip install -r requirements.txt   # if using Python
    ```
3. Access the API endpoint:
    ```
    /get_volumetric
    ```
4. Open the visualization in a browser to see interactive 3D volumetric output

---

## Project Structure

```
formula-to-3d-prototype/
├── engine/
│   ├── compute.py              # Example formula computation (E = mc² placeholder)
│   └── fetch_iers_data.py      # Script to pull, filter, and convert IERS data into JSON
├── api/                        # REST API endpoints (optional)
├── docs/                       # GitHub Pages deployment folder
│   ├── index.html
│   └── volumetric_data.json
├── requirements.txt
├── README.md
└── LICENSE
```

## Current Status
- Static frontend deployed via GitHub Pages at https://toko.eckohaus.com
- Volumetric displays:
	•	**Left**: IERS dataset (auto-updated daily at 02:00 UTC via GitHub Actions)
	•	**Right**: Formula placeholder array from compute.py
- CI/CD pipeline fetches and pushes new data to gh-pages

## Future Extensions
- Replace placeholder formula with more complex physics models (QCD, energy fields, etc.)
- Add additional scientific datasets
- Integrate ML pipelines for prediction and simulation
- Extend CMS-based user interface
- Deploy as a SaaS platform

---

## License
This project is licensed under the **Creative Commons** License. See the LICENSE file for details.
Please note: The IERS data remains subject to its own attribution and usage requirements.
