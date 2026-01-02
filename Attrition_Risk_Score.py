#Load Data (PyCharm)
import pandas as pd

df = pd.read_csv("HR_Analytics_Cleaned.csv")

#Convert Attrition to Numeric
df["Attrition_Flag"] = df["Attrition"].map({"Yes": 1, "No": 0})


#Create Individual Risk Flags
#1Low Salary Risk
df["Low_Salary_Risk"] = df["MonthlyIncome"].apply(
    lambda x: 1 if x < 5000 else 0
)

#2 OverTime Risk
df["OverTime_Risk"] = df["OverTime"].map({"Yes": 1, "No": 0})


#3 Low Job Satisfaction Risk
df["Low_JobSatisfaction_Risk"] = df["JobSatisfaction"].apply(
    lambda x: 1 if x <= 2 else 0
)

#4 Low Work-Life Balance Risk
df["Low_WorkLife_Risk"] = df["WorkLifeBalance"].apply(
    lambda x: 1 if x <= 2 else 0
)

#5 Short Tenure Risk (Early Exit)
df["Low_Tenure_Risk"] = df["YearsAtCompany"].apply(
    lambda x: 1 if x <= 2 else 0
)


#Create ATTRITION RISK SCORE
df["Attrition_Risk_Score"] = (
    df["Low_Salary_Risk"] +
    df["OverTime_Risk"] +
    df["Low_JobSatisfaction_Risk"] +
    df["Low_WorkLife_Risk"] +
    df["Low_Tenure_Risk"]
)


#Convert Score into Risk Category (HR-Friendly)
def risk_label(score):
    if score >= 4:
        return "High Risk"
    elif score >= 2:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Attrition_Risk_Level"] = df["Attrition_Risk_Score"].apply(risk_label)


#See the Result
print(df[[
    "Attrition",
    "MonthlyIncome",
    "OverTime",
    "YearsAtCompany",
    "Attrition_Risk_Score",
    "Attrition_Risk_Level"
]].head(10))


#OPTIONAL VALIDATION (Very Powerful) Check if High Risk employees actually left more:
print(
    df.groupby("Attrition_Risk_Level")["Attrition_Flag"].mean() * 100
)



##Visualize Attrition Risk Distribution
#LOAD DATA
import matplotlib.pyplot as plt

#EMPLOYEE COUNT BY RISK LEVEL
risk_counts = df["Attrition_Risk_Level"].value_counts()
print(risk_counts)

#BAR CHART: RISK DISTRIBUTION
plt.figure(figsize=(6, 4))
risk_counts.plot(kind="bar")

plt.title("Employee Distribution by Attrition Risk Level")
plt.xlabel("Attrition Risk Level")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#ATTRITION RATE BY RISK LEVEL
risk_attrition = (
    df.groupby("Attrition_Risk_Level")["Attrition_Flag"]
    .mean() * 100
)

print(risk_attrition)


#BAR CHART: ATTRITION % BY RISK LEVEL
plt.figure(figsize=(6, 4))
risk_attrition.plot(kind="bar")

plt.title("Attrition Rate by Risk Level")
plt.xlabel("Attrition Risk Level")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()




##Salary vs Attrition Risk (Heatmap-style insight)

#CREATE SALARY BANDS
df["Salary_Band"] = pd.cut(
    df["MonthlyIncome"],
    bins=[0, 3000, 7000, df["MonthlyIncome"].max()],
    labels=["Low Salary", "Medium Salary", "High Salary"]
)

#CREATE SUMMARY TABLE
salary_risk_table = pd.crosstab(
    df["Salary_Band"],
    df["Attrition_Risk_Level"]
)

print(salary_risk_table)


#VISUALIZE (Heatmap-Style Bar Chart)
salary_risk_table.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Attrition Risk Distribution by Salary Band")
plt.xlabel("Salary Band")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.legend(title="Attrition Risk Level")
plt.tight_layout()
plt.show()


#Attrition % instead of count:
salary_risk_rate = (
    df.groupby(["Salary_Band", "Attrition_Risk_Level"])["Attrition_Flag"]
    .mean()
    .unstack() * 100
)

print(salary_risk_rate)
