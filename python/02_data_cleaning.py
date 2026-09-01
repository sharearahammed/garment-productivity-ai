import pandas as pd

# Load processed data
try:
    df = pd.read_csv("data/processed/garment_productivity_sql.csv")
except FileNotFoundError:
    raise FileNotFoundError(
        "Processed SQL file not found. Run 01_data_loading.py first to save the data."
    )

print("Original shape:", df.shape)

# Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text columns
text_columns = [
    "quarter",
    "department",
    "day_name"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype("string").str.strip()

# Standardize department names
if "department" in df.columns:
    df["department"] = df["department"].replace({
        "sweing": "Sewing",
        "finishing": "Finishing"
    })

# Convert date
if "production_date" in df.columns:
    df["production_date"] = pd.to_datetime(
        df["production_date"],
        errors="coerce"
    )

# Numeric columns
numeric_columns = [
    "targeted_productivity",
    "smv",
    "wip",
    "over_time",
    "incentive",
    "idle_time",
    "idle_men",
    "no_of_style_change",
    "no_of_workers",
    "actual_productivity"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Save cleaned data
df.to_csv(
    "data/processed/garment_productivity_cleaned.csv",
    index=False
)

print("\nCleaned data saved successfully!")
print("Final shape:", df.shape)