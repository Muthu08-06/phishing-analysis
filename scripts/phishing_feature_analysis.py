import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.csv')

# Split phishing and legitimate
phishing = df[df['Result'] == -1]
legit = df[df['Result'] == 1]

# Count mean values for each group (shows % of 1s)
phishing_means = phishing.mean()
legit_means = legit.mean()

# Pick top 10 differing features
difference = (phishing_means - legit_means).abs().sort_values(ascending=False).head(10)

# Plot them
plt.figure(figsize=(10, 6))
difference.plot(kind='barh', color='firebrick')
plt.xlabel('Difference in Mean Values')
plt.title('Top 10 Features that Differentiate Phishing from Legitimate')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
