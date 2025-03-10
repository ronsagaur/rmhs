import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df_women = pd.read_csv("cleaned_data.csv")


# Summary Statistics
print("\nSummary Statistics:")
print(df_women.describe())

# Employment Distribution
employment_counts = df_women["Employment_Category"].value_counts()
print("\nEmployment Distribution:\n", employment_counts)

# Visualization: Employment Distribution
plt.figure(figsize=(10,5))
sns.barplot(x=employment_counts.index, y=employment_counts.values, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("Employment Category")
plt.ylabel("Count")
plt.title("Distribution of Employment Among Women")
plt.show()

# Employment by Age
plt.figure(figsize=(8,5))
sns.boxplot(x="Employment_Category", y="RO5/Age", data=df_women, palette="pastel")
plt.xticks(rotation=45)
plt.xlabel("Employment Category")
plt.ylabel("Age")
plt.title("Age Distribution Across Employment Categories")
plt.show()

# Employment by Caste
plt.figure(figsize=(8,5))
sns.countplot(x="ID13/ Caste_Category", hue="Employment_Category", data=df_women, palette="Set2")
plt.xlabel("Caste Category")
plt.ylabel("Count")
plt.title("Employment by Caste")
plt.legend(title="Employment Category", bbox_to_anchor=(1,1))
plt.show()

# Employment by Education Level
plt.figure(figsize=(8,5))
sns.countplot(x="ED2/Education", hue="Employment_Category", data=df_women, palette="coolwarm")
plt.xlabel("Education Level (0 = Illiterate, 1 = Literate)")
plt.ylabel("Count")
plt.title("Employment by Education Level")
plt.legend(title="Employment Category", bbox_to_anchor=(1,1))
plt.show()

# Employment by Income
plt.figure(figsize=(8,5))
sns.boxplot(x="Employment_Category", y="Income", data=df_women, palette="muted")
plt.xticks(rotation=45)
plt.xlabel("Employment Category")
plt.ylabel("Household Income")
plt.title("Household Income Across Employment Categories")
plt.show()
