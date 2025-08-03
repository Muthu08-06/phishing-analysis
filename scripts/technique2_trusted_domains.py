import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.csv")

# Filter only phishing samples
phishing = df[df["Result"] == -1]

print("🔍 Total Phishing Samples:", len(phishing))

print("\n📌 Request_URL (external object links):")
print(phishing["Request_URL"].value_counts())

print("\n📌 URL_of_Anchor (external anchor links):")
print(phishing["URL_of_Anchor"].value_counts())
