import requests
import pandas as pd

# Adzuna API credentials
APP_ID = '962be41e'
APP_KEY = '2cc2cb3ac6ce1fb5c2e41701491b47b3'

# API endpoint
url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

# API parameters
params = {
    'app_id': APP_ID,
    'app_key': APP_KEY,
    'results_per_page': 50,
    'what': 'data analyst',  # Job title
    'where': 'New York',  # Location
}

# Fetch data
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()['results']
    df = pd.DataFrame(data)
    df.to_csv('job_data.csv', index=False)
    print("Data saved to job_data.csv")
else:
    print("Error:", response.status_code)
