import numpy as np

def generate_formula_data():
    """
    Generate a grid of points for the formula volumetric display.
    Example: placeholder formula E = mc^2 mapping.
    Returns a list of dicts: [{"x": ..., "y": ..., "z": ...}, ...]
    """
    formula_points = [
        {"x": x, "y": y, "z": x * y * 0.1}  # simple demo mapping
        for x in range(10)
        for y in range(10)
    ]
    return formula_points
