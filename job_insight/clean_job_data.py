import pandas as pd
import ast  # Import the ast module for safe evaluation

# Load the raw job data
df = pd.read_csv('job_data.csv')

# Extract key fields, handling missing values
df_cleaned = pd.DataFrame({
    'title': df['title'],
    'company': df['company'].apply(lambda x: eval(x).get('display_name') if pd.notna(x) else 'N/A'),
    'location': df['location'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else 'N/A'),  # Use ast.literal_eval here
    'salary_min': df['salary_min'],
    'salary_max': df['salary_max'],
    'redirect_url': df['redirect_url']
})

# Extract location name for visualization
df_cleaned['location_name'] = df_cleaned['location'].apply(
    lambda x: x.get('display_name') if isinstance(x, dict) and 'display_name' in x else 'N/A'
)

# Save the cleaned data to a CSV file
df_cleaned.to_csv('cleaned_job_data.csv', index=False)

print("✅ Cleaned data saved to cleaned_job_data.csv")
