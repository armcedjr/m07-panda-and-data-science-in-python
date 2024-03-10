import pandas as pd

# Load the dataset
df = pd.read_csv('telco_churn.csv')  # Replace 'your_dataset.csv' with the actual file name

# Explore the dataset
print("Head of the DataFrame:")
print(df.head())  # Display the first few rows of the dataframe
print("\nInfo about the DataFrame:")
print(df.info())  # Display information about the dataframe (data types, missing values, etc.)

# Modify the dataset (Example: Handling missing values)
# Replace missing values in a specific column with the mean of that column
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Modify the dataset (Example: Converting data types)
# Convert a column to datetime format
df['date_column'] = pd.to_datetime(df['date_column'])

# Modify the dataset (Example: Perform feature engineering)
# Create a new column based on existing columns
df['new_column'] = df['existing_column1'] + df['existing_column2']

# Save the preprocessed dataset
df.to_csv('preprocessed_dataset.csv', index=False)  # Save the dataframe to a new CSV file
