# Project Notes

## Project Summary
This repository contains a garment productivity analytics project that combines SQL processing, Python analysis, and Power BI reporting.

## Workflow
- Raw data is stored in the `data/raw` folder
- SQL scripts create the database and table structure
- Python scripts clean, analyze, and model the dataset
- Outputs are saved under `python/outputs`
- Power BI dashboard visualizes the key results

## Important Files
- `python/01_data_loading.py` - loads SQL data into pandas
- `python/02_data_cleaning.py` - cleans the dataset
- `python/03_eda.py` - exploratory data analysis
- `python/04_regression_model.py` - regression model comparison
- `python/05_classification_model.py` - target achievement classifier
- `python/06_prediction_export.py` - exports prediction CSV
- `python/07_feature_importance.py` - explains model drivers

## Future Enhancements
- add SHAP explanations
- train and save final model artifacts in `python/models`
- automate the data pipeline
- extend dashboard with drill-through filters
