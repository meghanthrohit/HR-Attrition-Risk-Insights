#ATTRITION vs EXPERIENCE (Clean Restart)
#Load Data
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics_Cleaned.csv")

#Convert Attrition to Numeric (CRITICAL)
df["Attrition_Flag"] = df["Attrition"].map({"Yes": 1, "No": 0})

#Attrition vs Total Working Years
experience_attrition = (
    df.groupby("TotalWorkingYears")["Attrition_Flag"]
    .mean()
    .reset_index()
)

experience_attrition["Attrition_Rate_%"] = (
    experience_attrition["Attrition_Flag"] * 100
)

print(experience_attrition.head())



#Plot (Clean & Readable)
plt.figure(figsize=(8, 5))
plt.plot(
    experience_attrition["TotalWorkingYears"],
    experience_attrition["Attrition_Rate_%"],
    marker="o"
)

plt.title("Attrition Rate vs Total Working Years")
plt.xlabel("Total Working Years (Experience)")
plt.ylabel("Attrition Rate (%)")
plt.grid(True)
plt.show()


#Attrition vs Years at Company (Tenure)
tenure_attrition = (
    df.groupby("YearsAtCompany")["Attrition_Flag"]
    .mean()
    .reset_index()
)

tenure_attrition["Attrition_Rate_%"] = (
    tenure_attrition["Attrition_Flag"] * 100
)

plt.figure(figsize=(8, 5))
plt.plot(
    tenure_attrition["YearsAtCompany"],
    tenure_attrition["Attrition_Rate_%"],
    marker="o",
    color="orange"
)

plt.title("Attrition Rate vs Years at Company")
plt.xlabel("Years at Company (Tenure)")
plt.ylabel("Attrition Rate (%)")
plt.grid(True)
plt.show()

