#Attrition Rate by Environment Satisfaction
import pandas as pd

df = pd.read_csv("HR_Analytics_Cleaned.csv")

env_attrition = (
    df.groupby("EnvironmentSatisfaction")["Attrition_Flag"]
    .mean()
    .reset_index()
)

env_attrition["Attrition_Rate_%"] = env_attrition["Attrition_Flag"] * 100

print("\nAttrition Rate by Environment Satisfaction:")
print(env_attrition)


#Visualize the Relationship
import matplotlib.pyplot as plt

plt.bar(
    env_attrition["EnvironmentSatisfaction"],
    env_attrition["Attrition_Rate_%"]
)

plt.title("Attrition Rate vs Work Environment Satisfaction")
plt.xlabel("Environment Satisfaction (1 = Low, 4 = High)")
plt.ylabel("Attrition Rate (%)")

plt.xticks([1, 2, 3, 4])

plt.show()


#Create Work Pressure Risk Column
df["Pressure_Risk"] = df["EnvironmentSatisfaction"].apply(
    lambda x: "High Pressure" if x <= 2 else "Low Pressure"
)

pressure_attrition = (
    df.groupby("Pressure_Risk")["Attrition_Flag"]
    .mean() * 100
)

print("\nAttrition Rate by Work Pressure:")
print(pressure_attrition)
