import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor

# Load cleaned data
try:
    df = pd.read_csv("data/processed/garment_productivity_cleaned.csv")
except FileNotFoundError:
    raise FileNotFoundError(
        "Cleaned data not found. Run 01_data_loading.py and 02_data_cleaning.py first."
    )

# Keep the columns needed for prediction
features = [
    "targeted_productivity",
    "smv",
    "wip",
    "over_time",
    "incentive",
    "idle_time",
    "idle_men",
    "no_of_style_change",
    "no_of_workers",
    "department",
    "team_no",
    "production_date"
]

# Ensure required columns exist
missing = [col for col in features if col not in df.columns]
if missing:
    raise ValueError(f"Missing required columns for prediction: {missing}")

# Prepare target
if "actual_productivity" not in df.columns:
    raise ValueError("actual_productivity column is required for prediction export.")

X = df[features].copy()
y = df["actual_productivity"]

# Convert date column to useful features
X["production_date"] = pd.to_datetime(X["production_date"], errors="coerce")
X["year"] = X["production_date"].dt.year
X["month"] = X["production_date"].dt.month
X["day"] = X["production_date"].dt.day

# Use only model input columns (drop raw date after extracting features)
model_features = [
    "targeted_productivity",
    "smv",
    "wip",
    "over_time",
    "incentive",
    "idle_time",
    "idle_men",
    "no_of_style_change",
    "no_of_workers",
    "department",
    "team_no",
    "year",
    "month",
    "day"
]

X = X[model_features]

numeric_features = [
    "targeted_productivity",
    "smv",
    "wip",
    "over_time",
    "incentive",
    "idle_time",
    "idle_men",
    "no_of_style_change",
    "no_of_workers",
    "team_no",
    "year",
    "month",
    "day"
]

categorical_features = ["department"]

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X)

# Prepare final output for Power BI
output = df[["production_date", "team_no", "targeted_productivity", "actual_productivity"]].copy()
output = output.rename(columns={
    "production_date": "Date",
    "team_no": "Team",
    "targeted_productivity": "Target",
    "actual_productivity": "Actual"
})

output["Predicted"] = predictions
output["Prediction_Error"] = output["Actual"] - output["Predicted"]
output["Status"] = np.where(
    output["Actual"] >= output["Target"],
    "Achieved",
    "Below Target"
)

# Optional: convert to the exact names requested in the prompt
output = output.rename(columns={
    "Date": "date",
    "Team": "team",
    "Target": "target",
    "Actual": "actual",
    "Predicted": "predicted",
    "Prediction_Error": "prediction_error",
    "Status": "status"
})

output_path = "python/outputs/predictions.csv"
output.to_csv(output_path, index=False)

print("Prediction export saved to:", output_path)
print(output.head())
