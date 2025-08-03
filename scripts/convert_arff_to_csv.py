import pandas as pd
from scipy.io import arff

# ✅ Correct full path to .arff file
data, meta = arff.loadarff('C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.arff')

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Convert bytes to strings (if needed)
df = df.applymap(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

# Save to CSV
df.to_csv('C:/Users/Premkumar/phishing-analysis/data/phishing_dataset.csv', index=False)

print("✅ CSV file saved successfully.")
