import pandas as pd

# Load cleaned HR data
df = pd.read_csv("HR_Analytics_Cleaned.csv")

# Create EmployeeNumber column
df.insert(0, "EmployeeNumber", range(1, len(df) + 1))

# Save new file for Power BI
df.to_csv("HR_Analytics_PowerBI.csv", index=False)

print("✅ EmployeeNumber column created successfully")
print(df.head())
