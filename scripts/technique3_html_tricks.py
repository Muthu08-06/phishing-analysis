import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.csv")

# Filter phishing entries only
phishing = df[df["Result"] == -1]

print("🔍 Total Phishing Samples:", len(phishing))

# Technique 3 - HTML/CSS Tricks
print("\n📌 Iframe Usage (invisible page layers):")
print(phishing["Iframe"].value_counts())

print("\n📌 Popup Windows Used:")
print(phishing["popUpWidnow"].value_counts())

print("\n📌 Right Click Disabled:")
print(phishing["RightClick"].value_counts())
