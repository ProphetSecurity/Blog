import pandas as pd
import plotly.express as px
import sys

# Check if the CSV file name is provided as a command-line argument
if len(sys.argv) < 1:
    print("Usage: python tuning_visualizer.py <filename.csv>")
    sys.exit(1)

# The first argument after the script name is the CSV file path
csv_file_path = sys.argv[1]

# Load the CSV file
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
    sys.exit(1)


# Ensure data types are correct
df['Total Time Investigating'] = pd.to_numeric(df['Total Time Investigating'], errors='coerce')
df['Efficacy'] = pd.to_numeric(df['Efficacy'], errors='coerce')
df['Alert Count'] = pd.to_numeric(df['Alert Count'], errors='coerce')

# Column Grouping by Color
group_columns = 'Alert Source'

# Create the bubble chart
fig = px.scatter(df,
                 x='Total Time Investigating',
                 y='Efficacy',
                 size='Alert Count',  # Bubble size
                 color=group_columns,  # Color based on the first grouping column
                 hover_data=['Alert Name', 'Alert Source', 'Alert Count', 'Total Time Investigating', 'Median Investigation Time', 'Efficacy'],
                 title='Alert Tuning Visualization',
                 labels={"color": group_columns})

# Improve layout and axis titles
fig.update_layout(xaxis_title='Total Time Spent (minutes)',
                  yaxis_title='Efficacy (%)',
                  xaxis_title_font=dict(size=18),  # Increase X-axis title font size
                  yaxis_title_font=dict(size=18))

# Show the plot
fig.show()
