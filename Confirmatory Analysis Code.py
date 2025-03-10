import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Define employment status: 1 = Employed, 0 = Inactive
df["Employed"] = df["Employment_Category"].apply(lambda x: 1 if x != "Inactive" else 0)

# Select relevant variables
features = ["RO5/Age", "ID13/ Caste_Category", "ED2/Education", "Income", "Size", "Cultivation"]
X = df[features]
y = df["Employed"]

# 🔹 Convert all feature columns to numeric
X = X.apply(pd.to_numeric, errors="coerce")

# Handle missing values
X.fillna(X.median(numeric_only=True), inplace=True)

# Scale Income to prevent large disparities
scaler = StandardScaler()
X["Income"] = scaler.fit_transform(X[["Income"]])

# Add constant for regression
X = sm.add_constant(X)

# Logistic Regression Model
logit_model = sm.Logit(y, X)
result = logit_model.fit()

# Print regression summary
print(result.summary())
