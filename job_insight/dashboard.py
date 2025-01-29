import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df_cleaned = pd.read_csv('cleaned_job_data.csv')

# Dashboard Title
st.title('Job Market Insights Dashboard')

# Top Job Titles
st.subheader('Top 10 Job Titles')
top_jobs = df_cleaned['title'].value_counts().head(10)
st.bar_chart(top_jobs)

# Salary Distribution
st.subheader('Salary Distribution')
fig, ax = plt.subplots()
sns.histplot(df_cleaned['salary_min'], kde=True, bins=20, ax=ax)
st.pyplot(fig)

# Top Locations
st.subheader('Top 10 Locations')
top_locations = df_cleaned['location_name'].value_counts().head(10)  # Use 'location_name' column
st.bar_chart(top_locations)
