import pandas as pd

# Load the raw job data
df = pd.read_csv('job_data.csv')

# Print the first few rows
print("First few rows of job_data.csv:")
print(df.head())

# Print the column names
print("\nColumn names in job_data.csv:")
print(df.columns)
