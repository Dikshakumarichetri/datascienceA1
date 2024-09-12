
import pandas as pd


# Assuming your CSV files are in the same directory where the script is running
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')


# Preview the first few rows of each dataset
print(dataset1.head())
print(dataset2.head())
print(dataset3.head())



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the specified location
dataset3 = pd.read_csv('dataset3.csv')

# Select behavioral variables for correlation analysis
behavioral_columns = ['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 'Loved', 'Intthg', 'Cheer']
behavioral_data = dataset3[behavioral_columns]

# Compute correlation matrix
correlation_matrix = behavioral_data.corr()

# Plotting the heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Behavioral Variables')
plt.tight_layout()

# Save or show the plot
plt.show()



