import pandas as pd

# Load the CSV file
df = pd.read_csv('C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.csv')

# Show first 5 records
print("🔍 Sample Records:")
print(df.head())

# Dataset structure
print("\n📊 Dataset Info:")
print(df.info())

# Class distribution (check if 'Result' or 'class' exists)
target_column = 'Result' if 'Result' in df.columns else 'class'
print("\n📌 Class Distribution:")
print(df[target_column].value_counts())
