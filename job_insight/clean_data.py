import os
import pandas as pd
import ast

# Use job_data.csv if the raw data is not cleaned yet, or use cleaned_job_data.csv if it's already cleaned
file_path = 'job_data.csv'  # or 'cleaned_job_data.csv' if you have already cleaned data

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found. Please ensure the correct file exists.")
else:
    # Load the job data
    df = pd.read_csv(file_path)
    print(f"Loaded data from {file_path}. The data has {len(df)} rows.")


    # Function to extract the 'display_name' from location data
    def extract_location(location):
        try:
            # Convert the string to a dictionary if it's a string representation of a dictionary
            if isinstance(location, str):
                location = ast.literal_eval(location)  # Safely evaluate the string as a dictionary

            # Extract 'display_name' if the location is a dictionary
            if isinstance(location, dict):
                return location.get('display_name', 'Unknown')
            else:
                return 'Unknown'
        except Exception as e:
            print(f"Error processing location: {e}")
            return 'Unknown'


    # Apply the function to the 'location' column
    df['location_name'] = df['location'].apply(extract_location)

    # Check how many 'location_name' values were successfully extracted
    successful_extractions = df['location_name'].notnull().sum()
    print(f"Successfully extracted {successful_extractions} location names.")

    # Save the cleaned data to a new CSV file
    df.to_csv('cleaned_job_data.csv', index=False)
    print("Cleaned data saved to 'cleaned_job_data.csv'.")
