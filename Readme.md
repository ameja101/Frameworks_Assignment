# 📊 CORD-19 Metadata Analysis & Streamlit Dashboard

This repository documents a full **data science workflow** using the **CORD-19 research dataset**.  
It covers data loading, cleaning, exploratory analysis, visualization, and an interactive Streamlit application.  

The project also captures the **learning journey** of handling large datasets, Git/GitHub workflow challenges, and building reproducible analysis.

---

## 📖 Project History

This project was developed in **5 structured parts**:

### 🔹 Part 1: Data Loading & Exploration
- Downloaded and worked with a subset of `metadata.csv` from the CORD-19 dataset (Kaggle).
- Loaded into a pandas DataFrame.
- Examined data structure, column types, missing values.
- Generated basic statistics for numerical columns.

### 🔹 Part 2: Data Cleaning & Preparation
- Identified and handled missing values (dropped high-missing columns).
- Converted publication dates to datetime format.
- Extracted publication year for time-series analysis.
- Created new features such as abstract word counts.

### 🔹 Part 3: Data Analysis & Visualization
- **Publication trends** over time.
- **Top journals** publishing COVID-19 research.
- **Frequent title words** via word frequency and word cloud.
- **Distribution of papers by source**.
- Visualizations saved in `charts/` directory for documentation.

### 🔹 Part 4: Streamlit Application
- Built an interactive app with:
  - Sidebar filters for year range & journal selection.
  - Data preview table.
  - Visualizations (time series, bar charts, word cloud, source distribution).
- Run locally with:
  ```bash
  streamlit run app.py
