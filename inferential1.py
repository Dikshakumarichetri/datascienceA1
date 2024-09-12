import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

dataset1 = pd.read_csv("dataset1.csv")
dataset2 = pd.read_csv("dataset2.csv")
dataset3 = pd.read_csv("dataset3.csv")
merged_df = dataset1.merge(dataset2, on='ID').merge(dataset3, on='ID')
merged_df = merged_df.dropna()
print(merged_df.head())

merged_df['Total_Screen_Time'] = merged_df[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)
wellbeing_mean = merged_df[['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Goodme', 'Clsep', 'Conf',
                            'Mkmind', 'Loved', 'Intthg', 'Cheer']].mean(axis=1)

X = merged_df[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']]
X = sm.add_constant(X)
y = wellbeing_mean

model = sm.OLS(y, X).fit()
print(model.summary())

predicted_y = model.predict(X)
comparison_df = pd.DataFrame({
    'Index': range(len(y)),
    'Actual Well-being': y,
    'Predicted Well-being': predicted_y
})

plt.figure(figsize=(12, 8))
plt.plot(comparison_df['Index'], comparison_df['Actual Well-being'], label='Actual Well-being', color='blue', linestyle='-', marker='o')
plt.plot(comparison_df['Index'], comparison_df['Predicted Well-being'], label='Predicted Well-being', color='red', linestyle='--', marker='x')

plt.title("Line Chart of Actual vs Predicted Well-being Scores", fontsize=18, fontweight='bold')
plt.xlabel("Index", fontsize=16)
plt.ylabel("Well-being Score", fontsize=16)
plt.legend(fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
