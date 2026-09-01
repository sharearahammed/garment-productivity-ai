import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "data/processed/garment_productivity_cleaned.csv"
)

print("Dataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nDescriptive Statistics:")
print(df.describe())

print("\nDepartment Productivity:")
print(
    df.groupby("department")["actual_productivity"]
      .mean()
      .sort_values(ascending=False)
)

# Productivity distribution
plt.figure(figsize=(10, 6))

sns.histplot(
    df["actual_productivity"],
    kde=True
)

plt.title("Actual Productivity Distribution")
plt.xlabel("Actual Productivity")
plt.ylabel("Frequency")

plt.savefig(
    "python/outputs/productivity_distribution.png",
    bbox_inches="tight"
)

plt.show()