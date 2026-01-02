#Average Experience by Attrition
import pandas as pd

df = pd.read_csv("HR_Analytics_Cleaned.csv")

experience_attrition = (
    df.groupby("Attrition")["TotalWorkingYears"]
    .mean()
    .reset_index()
)

print("\nAverage Total Working Years by Attrition:")
print(experience_attrition)


#Visualize Experience vs Attrition
import matplotlib.pyplot as plt

plt.bar(
    experience_attrition["Attrition"],
    experience_attrition["TotalWorkingYears"]
)

plt.title("Average Experience by Attrition")
plt.xlabel("Attrition")
plt.ylabel("Total Working Years")

plt.show()


#Create Experience Risk Bands
df["Experience_Risk"] = df["TotalWorkingYears"].apply(
    lambda x: "High Risk" if x < 5 else "Low Risk"
)

experience_risk_attrition = (
    df.groupby("Experience_Risk")["Attrition_Flag"]
    .mean() * 100
)

print("\nAttrition Rate by Experience Risk:")
print(experience_risk_attrition)
