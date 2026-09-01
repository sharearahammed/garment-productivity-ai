# Garment Productivity AI

A data-driven productivity analytics and prediction project for the garment manufacturing industry. This project focuses on analyzing workforce productivity, identifying operational bottlenecks, and forecasting whether productivity targets will be achieved.

## Overview

The project combines:

- SQL-based data storage and retrieval
- Python-based data cleaning and exploratory analysis
- Machine learning for regression and classification
- Explainable AI for feature importance analysis
- Power BI dashboarding for business reporting and decision-making

## Business Objective

The main goal is to improve operational efficiency by understanding which factors most strongly influence productivity and predicting whether daily targets will be achieved based on process and workforce variables.

## Project Workflow

1. Load production data from SQL Server
2. Clean and preprocess the dataset
3. Perform exploratory data analysis (EDA)
4. Train and compare regression models
5. Build a classification model for target achievement
6. Generate feature importance insights
7. Export prediction results for dashboarding
8. Visualize insights in Power BI

## Repository Structure

```text
garment-productivity-ai/
├── data/
│   ├── README.md
│   ├── raw/
│   │   └── garments_worker_productivity.csv
│   └── processed/
│       ├── garment_productivity_sql.csv
│       ├── garment_productivity_cleaned.csv
│       └── ...
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_insert_data.sql
│   └── 04_analysis_queries.sql
├── python/
│   ├── 01_data_loading.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_regression_model.py
│   ├── 05_classification_model.py
│   ├── 06_prediction_export.py
│   ├── 07_feature_importance.py
│   ├── requirements.txt
│   ├── models/
│   └── outputs/
├── powerbi/
│   └── Garment_Productivity_Analytics.pbix
├── reports/
│   ├── project_report.pdf
│   └── presentation.pptx
├── screenshots/
│   ├── dashboard_overview.png
│   ├── workforce_analysis.png
│   └── prediction_dashboard.png
├── README.md
├── LICENSE
└── .gitignore
```

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SQLAlchemy
- PyODBC
- SQL Server
- Power BI

## Dataset

The project uses garment worker productivity data, including variables such as:

- production date
- quarter
- department
- team number
- SMV
- WIP
- overtime
- incentive
- idle time
- worker count
- actual productivity
- target productivity

## Key Outputs

- cleaned productivity dataset
- exploratory visualizations
- regression model comparison
- classification model performance metrics
- feature importance ranking
- prediction CSV for Power BI

## Setup Instructions

### 1. Create a Python environment

```bash
python -m venv .venv
```

### 2. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r python/requirements.txt
```

### 4. Run the Python pipeline

```bash
python python/01_data_loading.py
python python/02_data_cleaning.py
python python/03_eda.py
python python/04_regression_model.py
python python/05_classification_model.py
python python/06_prediction_export.py
python python/07_feature_importance.py
```

## SQL Database Setup

The SQL scripts under the `sql/` folder can be used to create the database and data tables used by the Python pipeline.

## Power BI Dashboard

The dashboard file in the `powerbi/` folder is used to present operational insights and prediction results for stakeholders.

## Use Cases

- monitor team productivity trends
- detect underperforming departments or shifts
- identify factors contributing to low productivity
- forecast whether productivity targets are achieved
- support management decisions with actionable insights

## Screenshots

The project includes visual outputs for key dashboard and analytics views.

- Executive Productivity Overview: `screenshots/Executive Productivity Overview.png`
- Manufacturing Operations: `screenshots/Manufacturing Operations.png`
- Workforce Analysis: `screenshots/Workforce Analysis.png`

## Contact

For project collaboration or questions, please contact the project maintainer.
