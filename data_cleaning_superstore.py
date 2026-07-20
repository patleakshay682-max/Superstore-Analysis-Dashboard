# ============================================
# Sales Data Cleaning - Superstore Dataset
# Author: Milind Katre
# ============================================

import pandas as pd

df = pd.read_csv("Superstore-selected-columns.csv")

print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

for col in ['Order Date', 'Ship Date']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

for col in categorical_columns:
    df[col] = df[col].str.strip()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_csv("cleaned_superstore.csv", index=False)

print("\nCleaning Completed Successfully!")
print("Cleaned dataset saved as 'cleaned_superstore.csv'")
