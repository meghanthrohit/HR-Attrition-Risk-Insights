#Attrition vs Years Since Last Promotion
import pandas as pd

df = pd.read_csv("HR_Analytics_Cleaned.csv")

promotion_attrition = (
    df.groupby("YearsAtCompany")["Attrition_Flag"]
    .mean()
    .reset_index()
)

promotion_attrition["Attrition_Rate_%"] = promotion_attrition["Attrition_Flag"] * 100

print("\nAttrition vs Years Since Last Promotion:")
print(promotion_attrition.head(10))


#Visualize Clearly
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.plot(
    promotion_attrition["YearsAtCompany"],
    promotion_attrition["Attrition_Rate_%"],
    marker="o"
)

plt.title("Attrition Rate vs Years Since Last Promotion")
plt.xlabel("Years Since Last Promotion")
plt.ylabel("Attrition Rate (%)")

plt.grid(True)
plt.show()


#Create Promotion Risk Column (Predictive Thinking)
df["Promotion_Risk"] = df["YearsSinceLastPromotion"].apply(
    lambda x: "High Risk" if x >= 4 else "Low Risk"
)

promotion_risk_summary = (
    df.groupby("Promotion_Risk")["Attrition_Flag"]
    .mean() * 100
)

print("\nAttrition Rate by Promotion Risk:")
print(promotion_risk_summary)
