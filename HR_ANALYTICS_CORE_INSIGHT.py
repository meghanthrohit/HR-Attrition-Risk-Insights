import pandas as pd

# Load cleaned data
df = pd.read_csv("HR_Analytics_Cleaned.csv")

# Attrition rate by overtime
overtime_attrition = df.groupby("OverTime")["Attrition_Flag"].mean().reset_index()

# Convert to percentage
overtime_attrition["Attrition_Rate_%"] = overtime_attrition["Attrition_Flag"] * 100

print("\nAttrition Rate by Overtime:")
print(overtime_attrition)

#Simple Visualization (PyCharm Safe)
import matplotlib.pyplot as plt

plt.bar(
    overtime_attrition["OverTime"],
    overtime_attrition["Attrition_Rate_%"]
)

plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")

plt.show()
