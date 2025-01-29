import pandas as pd
import plotly.express as px

# Load the cleaned job data
df = pd.read_csv('cleaned_job_data.csv')

# Check if data is loaded correctly
print(df.head())

# Get the top 10 job titles
job_titles = df['title'].value_counts().head(10)

# Create a horizontal bar chart for better readability
fig = px.bar(job_titles,
             x=job_titles.values,
             y=job_titles.index,
             orientation='h',  # Horizontal bars
             title="Top 10 Job Titles",
             labels={'x': 'Count', 'y': 'Job Title'})

# Improve layout for better spacing
fig.update_layout(
    title_x=0.5,  # Centers the title
    title_y=0.95,  # Moves title slightly higher
    yaxis=dict(title="Job Title"),  # Ensure the y-axis title is clear
    xaxis=dict(title="Count"),  # Label the x-axis
    margin=dict(l=150, r=20, t=100, b=50),  # Increased top margin (t=100)
    height=500,  # Adjust height for compactness
)

# Show the plot
fig.show()
