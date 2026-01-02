import pandas as pd

# Load data
df = pd.read_csv("HR_Analytics_Cleaned.csv")

# Average salary by attrition
salary_attrition = df.groupby("Attrition")["MonthlyIncome"].mean().reset_index()

print("\nAverage Monthly Income by Attrition:")
print(salary_attrition)


#Visual Comparison (PyCharm Friendly)
import matplotlib.pyplot as plt

plt.bar(
    salary_attrition["Attrition"],
    salary_attrition["MonthlyIncome"]
)

plt.title("Average Monthly Income by Attrition")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")

plt.show()


#Create Salary Risk Bands (Very Important)
df["Salary_Risk"] = df["MonthlyIncome"].apply(
    lambda x: "High Risk" if x < 5000 else "Low Risk"
)

# Attrition rate by salary risk
salary_risk_attrition = df.groupby("Salary_Risk")["Attrition_Flag"].mean() * 100

print("\nAttrition Rate by Salary Risk:")
print(salary_risk_attrition)
