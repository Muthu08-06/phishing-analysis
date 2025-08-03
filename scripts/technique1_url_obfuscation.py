import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.csv")

# Filter phishing sites
phishing = df[df["Result"] == -1]

# Technique 1 - URL Obfuscation

print("🔍 Total Phishing Samples:", len(phishing))

print("\n📌 Having IP Address (instead of domain):")
print(phishing["having_IP_Address"].value_counts())

print("\n📌 Using URL Shortening Service:")
print(phishing["Shortining_Service"].value_counts())
