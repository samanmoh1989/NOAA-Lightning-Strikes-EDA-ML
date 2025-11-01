
# ⚡ Lightning Strikes Analysis (2018) — Coursera‑Style End‑to‑End Project

This repository contains a complete, Coursera‑style data science project that analyzes **global lightning strikes during 2018** using NOAA data.  
It includes **data loading, cleaning, EDA (temporal & spatial), statistical analysis, and baseline predictive modeling** (Linear Regression, Random Forest, XGBoost), plus **interactive maps** and a ready‑to‑run environment.

---

## 📁 Project Structure
```
lightning_analysis/
├─ data/                    # Put the dataset CSV file here (e.g., lightning strikes dataset.csv)
├─ notebooks/
│  └─ analysis.ipynb        # Main Jupyter notebook with all steps
├─ scripts/
│  └─ utils.py              # Optional helper functions (placeholders)
├─ outputs/                 # Generated charts & maps (HTML/PNG)
├─ README.md                # (this file)
└─ .gitignore               # ignores checkpoints, cache, outputs
```

---

## 📦 Dataset
- **Source:** NOAA Lightning Strikes (2018) — available via Kaggle.
- **Expected CSV columns (example):**  
  `date`, `number_of_strikes`, `center_point_geom` where `center_point_geom` looks like `POINT(-78.4 29)`

> After download, place the CSV in:  
> `data/lightning strikes dataset.csv`  
> (You can rename it to `lightning.csv` if you prefer. Update the notebook path accordingly.)

---

## 🚀 Quickstart

### 1) Create environment & install requirements
```bash
# Option A: pip
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

pip install -r requirements.txt
python -m ipykernel install --user --name lightning-env --display-name "Python (lightning)"

# Optional: JupyterLab
jupyter lab
# or classic
jupyter notebook
```

### 2) Open the notebook
Open `notebooks/analysis.ipynb` and run cells from top to bottom.  
If needed, adjust the dataset path (e.g., `E:\Data science\projects\lightning_analysis\data\lightning.csv`).

---

## 🧭 Workflow Overview (Notebook Sections)

1. **Introduction** — project goals, data source, and scope.
2. **Data Loading** — read CSV with `pandas`.
3. **Cleaning & Parsing** — extract `latitude` & `longitude` from `center_point_geom`.
4. **Temporal EDA** — monthly trend of lightning strikes.
5. **Spatial EDA** — interactive maps (Folium Heatmap & Clustered Points).
6. **Statistical Analysis** — distributions & correlation heatmap.
7. **Modeling (Baselines)** — Linear Regression, Random Forest, XGBoost.
8. **Feature Importance** — interpret the model using XGBoost importances.
9. **Outputs** — export interactive HTML maps into `outputs/`.

---

## 📊 Results (Sample)

### Temporal Pattern
Lightning activity shows a strong **seasonal** pattern with a peak in **August**.

### Spatial Pattern
Tropical/subtropical belts exhibit the **highest density**; higher latitudes show fewer strikes.

### Baseline Models (illustrative)
| Model              | MAE   | R²     |
|--------------------|-------|--------|
| Linear Regression  | ~14.5 | ~0.001 |
| Random Forest      | ~14.4 | -0.09  |
| **XGBoost**        | **~13.6** | **~0.08** |

> These baseline metrics are expected because we only use `latitude`, `longitude`, and `month`.  
> Adding meteorological features (temperature, humidity, pressure) should improve performance.

---

## 🌍 Interactive Maps
Running the notebook generates:
- `outputs/lightning_heatmap.html`
- `outputs/lightning_points_cluster.html`
- (optional) `outputs/lightning_heatmap_august.html`

Open these files in a browser to explore the data interactively.

---

## 🧪 Reproducibility Checklist
- Python and package versions pinned in `requirements.txt`
- Random seeds used where applicable (`random_state=42`)
- Notebook cells are ordered and documented
- Data path is configurable at the top of the notebook

---

## 🛠 Tech Stack
- **Python:** pandas, numpy
- **Viz:** matplotlib, seaborn, folium
- **ML:** scikit-learn, xgboost
- **Notebook:** jupyter / jupyterlab

---

## 📌 Roadmap / Ideas
- Enrich features with **meteorological variables** (temperature, humidity, pressure, precipitation).
- Try **spatiotemporal models** (e.g., gradient boosting with lag features).
- Add **elevation/terrain** data and **distance to equator** features.
- Deploy a simple **dashboard** (Streamlit) to browse maps and trends.

---

## 🤝 Acknowledgments
- NOAA (National Oceanic and Atmospheric Administration) for providing lightning products/data.
- Kaggle community for hosting prepared datasets.

---

## 📄 License
MIT — feel free to use, modify, and share with attribution.
