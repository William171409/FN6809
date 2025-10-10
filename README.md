<!-- # FN6809
This repo contains all the materials of FN6809 Linear Regression project -->

# Used Cars Price Modeling

Quick overview: open `linear_final.ipynb`.

This repository contains an end-to-end exploratory / linear-modeling notebook for used car prices. The notebook performs cleaning, feature engineering, encoding, model fitting (OLS, WLS, robust), diagnostics, variable selection (SFS, Lasso), and PCA experiments.

## Files
- `linear_final.ipynb` — Main Jupyter Notebook (open this for a quick interactive overview and walkthrough).
- `linear_utils.py` — Utility functions referenced by the notebook (keep this in the same directory as the notebook).
- `used_cars.csv` — Raw dataset used by the notebook (download and place in the same directory).

## Quickstart (recommended)
1. Place these files in the same directory:
    - `linear_final.ipynb`
    - `linear_utils.py`
    - `used_cars.csv` (download the dataset and save with this exact filename)

2. Start Jupyter:
    jupyter notebook
    or
    jupyter lab

3. Open `linear_final.ipynb` in the notebook UI and run cells in order. The notebook is structured so earlier cells define helper functions and load data, later cells perform modeling and diagnostics.
