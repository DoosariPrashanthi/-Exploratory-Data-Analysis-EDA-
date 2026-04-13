import pandas as pd

df = pd.read_csv("mobile_price_dataset.csv")
print(df.head())
print(df.describe())
print(df.info())
import matplotlib.pyplot as plt

df.hist(figsize=(10,8))
plt.show()
import seaborn as sns

sns.boxplot(x=df["Price_USD"])
plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
sns.pairplot(df)
plt.show()
