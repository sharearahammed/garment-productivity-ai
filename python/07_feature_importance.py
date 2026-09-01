import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

# Load cleaned data
try:
    df = pd.read_csv("data/processed/garment_productivity_cleaned.csv")
except FileNotFoundError:
    raise FileNotFoundError(
        "Cleaned data not found. Run 01_data_loading.py and 02_data_cleaning.py first."
    )

# Create classification target
if "actual_productivity" in df.columns and "targeted_productivity" in df.columns:
    df["target_label"] = np.where(
        df["actual_productivity"] >= df["targeted_productivity"],
        1,
        0
    )
else:
    raise ValueError("Required columns for classification target are missing.")

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
    "team_no"
]

target = "target_label"

X = df[features]
y = df[target]

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
    "team_no"
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
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])

pipeline.fit(X_train, y_train)

# Extract feature importance after one-hot encoding
# For original features, we need to map back from transformed columns.
transformed_features = pipeline.named_steps["preprocessor"].get_feature_names_out()
importances = pipeline.named_steps["model"].feature_importances_

feature_importance_df = pd.DataFrame({
    "Feature": transformed_features,
    "Importance": importances
})

feature_importance_df = feature_importance_df.sort_values(
    by="Importance",
    ascending=False
).reset_index(drop=True)

output_path = "python/outputs/feature_importance.csv"
feature_importance_df.to_csv(output_path, index=False)

print("Feature importance saved to:", output_path)
print(feature_importance_df.head(20))

# Optional: aggregate to original feature names when possible
# This keeps the output easier to read.
original_feature_names = numeric_features + categorical_features
feature_importance_df["OriginalFeature"] = feature_importance_df["Feature"].str.replace(
    "num__|cat__",
    "",
    regex=True
)

# Keep only top features and sort
print("\nTop features by importance:")
print(feature_importance_df[["OriginalFeature", "Importance"]].head(10))
