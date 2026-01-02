#Attrition Rate by Overtime
import pandas as pd

df = pd.read_csv("HR_Analytics_Cleaned.csv")

overtime_attrition = (
    df.groupby("OverTime")["Attrition_Flag"]
    .mean()
    .reset_index()
)

overtime_attrition["Attrition_Rate_%"] = overtime_attrition["Attrition_Flag"] * 100

print("\nAttrition Rate by Overtime:")
print(overtime_attrition)

#Visualize (Clear & Simple)
import matplotlib.pyplot as plt

plt.bar(
    overtime_attrition["OverTime"],
    overtime_attrition["Attrition_Rate_%"]
)

plt.title("Attrition Rate vs Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")

plt.show()


#Create Overtime Risk Column
df["Overtime_Risk"] = df["OverTime"].apply(
    lambda x: "High Risk" if x == "Yes" else "Low Risk"
)

risk_summary = (
    df.groupby("Overtime_Risk")["Attrition_Flag"]
    .mean() * 100
)

print("\nAttrition Rate by Overtime Risk:")
print(risk_summary)
