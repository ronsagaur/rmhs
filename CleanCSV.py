import pandas as pd

# Load the dataset (replace 'your_file.csv' with actual file path)
df = pd.read_csv('ihds_full_data.csv')

# Display basic infoss
print("Initial Data Info:")
print(df.info())

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values[missing_values > 0])

# Convert necessary columns to categorical for better analysis
categorical_cols = ["RO7/ Activity_Status", "RO3/Sex", "ID13/ Caste_Category", "ED2/Education", "STATEID", "Cultivation"]
df[categorical_cols] = df[categorical_cols].astype('category')

# Filter dataset for women (Gender = 2)
df_women = df[df["RO3/Sex"] == 2]

# Recode occupation categories (grouping similar ones)
occupation_mapping = {
    1: "Cultivation",
    2: "Agriculture",
    3: "Agriculture",
    4: "Non-Agriculture",
    5: "Self-Employed",
    6: "Self-Employed",
    7: "Self-Employed",
    8: "Salaried",
    9: "Professional",
    10: "Inactive",
    11: "Inactive",
    12: "Inactive",
    13: "Inactive",
    14: "Inactive",
    15: "Others"
}
df_women["Employment_Category"] = df_women["RO7/ Activity_Status"].map(occupation_mapping)

# Display cleaned dataset summary
print("\nCleaned Data Info:")
print(df_women.info())

# Save cleaned dataset for further analysis
df_women.to_csv("cleaned_data.csv", index=False)
