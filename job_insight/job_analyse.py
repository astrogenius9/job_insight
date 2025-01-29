import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv('job_data.csv')
print(df.head())
job_titles = df['title'].value_counts().head(10)
print(job_titles)
locations = df['location'].value_counts().head(10)
print(locations)

sns.histplot(df['salary_min'], kde=True, bins=20)
plt.title('Salary Distribution')
plt.show()