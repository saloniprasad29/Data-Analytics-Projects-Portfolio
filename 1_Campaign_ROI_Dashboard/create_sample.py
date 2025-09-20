import pandas as pd

# Load full dataset
df = pd.read_csv("data/raw_campaign/marketing_campaign.csv")

# Take a sample (e.g., 5000 rows)
sample = df.sample(n=5000, random_state=42)

# Save the sample dataset
sample.to_csv("1_Campaign_ROI_Dashboard/data/raw_campaign/marketing_campaign_sample.csv", index=False)

print("✅ Sample dataset created: marketing_campaign_sample.csv")
