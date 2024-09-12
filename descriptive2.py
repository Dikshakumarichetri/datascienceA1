import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the datasets
df2 = pd.read_csv('dataset2.csv')  # Contains screen time data
df3 = pd.read_csv('dataset3.csv')  # Contains well-being indicators

# Merge datasets on 'ID'
df_merged = pd.merge(df2, df3, on='ID', how='inner')

# Descriptive statistics
descriptive_stats = df_merged.describe()
print("Descriptive Statistics:\n", descriptive_stats)

# Correlation between screen time and well-being indicators
correlation = df_merged[['C_we', 'C_wk', 'G_we', 'S_we', 'T_we', 'Optm', 'Relx', 'Usef']].corr()
print("Correlation Matrix:\n", correlation)

# Create a total screen time column
df_merged['Total_Screen_Time'] = df_merged[['C_we', 'C_wk', 'G_we', 'S_we', 'T_we']].sum(axis=1)

# Define bins for screen time and create a new column for categories
bins = [0, 10, 20, 30, 40, 50]  # Adjust bins according to your data range
labels = ['0-10 hours', '10-20 hours', '20-30 hours', '30-40 hours', '40-50 hours']
df_merged['Screen_Time_Category'] = pd.cut(df_merged['Total_Screen_Time'], bins=bins, labels=labels)

# Group by screen time categories and calculate the mean of well-being indicators
grouped_summary = df_merged.groupby('Screen_Time_Category')[['Optm', 'Relx', 'Usef']].mean()
print("Grouped Summary by Screen Time Category:\n", grouped_summary)

# Plotting the bar graph for average well-being indicators by screen time category
grouped_summary.plot(kind='bar', figsize=(10, 6))
plt.title('Average Well-Being Indicators by Total Screen Time Category')
plt.xlabel('Total Screen Time (Hours)')
plt.ylabel('Average Scores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
