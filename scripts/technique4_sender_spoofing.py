import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.csv")

# Filter phishing samples only
phishing = df[df["Result"] == -1]

print("🔍 Total Phishing Samples:", len(phishing))

# Technique 4 - Email Spoofing Indicator
print("\n📧 Submitting to Email (Spoofing Indicator):")
print(phishing["Submitting_to_email"].value_counts())
