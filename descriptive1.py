
# Step 1 : Importing Dataset into python
import pandas as pd
# Dataset import code

dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')
# Preview the first few rows of each dataset
print(dataset1.head())
print(dataset2.head())
print(dataset3.head())
# Step 2: Cleaning Dataset -Clean dataset1 by removing unnecessary columns (if there are any)
dataset1_cleaned = dataset1.drop(columns=[col for col in dataset1.columns if 'Unnamed' in col])
# Step 3 : Merging Dataset - Merge the datasets on the 'ID' column
merged_data = pd.merge(dataset1_cleaned, dataset2, on='ID')
merged_data = pd.merge(merged_data, dataset3, on='ID')
# Step 4: Previewing Merged Dataset
print(merged_data.head())
# Step 5 Define the screen time columns
screen_time_columns = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']
# Step 6Descriptive statistics for screen time variables
screen_time_columns = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']
screen_time_stats = merged_data[screen_time_columns].describe()
print(screen_time_stats)
# Step 7 Descriptive statistics for well-being variables
well_being_columns = ['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 'Loved', 'Intthg', 'Cheer']
well_being_stats = merged_data[well_being_columns].describe()
print(well_being_stats)
# Step 8 Calculate Mean Screen Time (Weekends vs. Weekdays) by Gender
import pandas as pd
# Calculate total screen time for weekends and weekdays by summing screen time for each device
merged_data['total_weekend_screen_time'] = merged_data[['C_we', 'G_we', 'S_we', 'T_we']].sum(axis=1)
merged_data['total_weekday_screen_time'] = merged_data[['C_wk', 'G_wk', 'S_wk', 'T_wk']].sum(axis=1)
# Calculate mean screen time for weekends and weekdays by gender
mean_screen_time_by_gender = merged_data.groupby('gender')[['total_weekend_screen_time', 'total_weekday_screen_time']].mean()
# Step 9 Display the mean screen time for weekends and weekdays by gender
print(mean_screen_time_by_gender)
import matplotlib.pyplot as plt
# Create a bar graph to compare the mean screen time for weekends and weekdays by gender
mean_screen_time_by_gender.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange'])
plt.title('Average Screen Time (Weekdays vs. Weekends) by Gender')
plt.ylabel('Mean Screen Time (hours)')
plt.xlabel('Gender (0 = Others, 1 = Male)')
plt.xticks(rotation=0)
plt.legend(['Weekend', 'Weekday'])
plt.grid(True)
plt.show()


