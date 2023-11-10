# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:16:40 2023
@author: Usman 
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_pie_chart_covid_cases(dataframe, time_period):
    """
    Function to create a pie chart for the distribution of COVID cases among countries.

    Arguments:
    dataframe -- A pandas DataFrame with countries as rows and time periods as columns.
    time_period -- A specific time period for which the pie chart is to be created.

    This function takes a DataFrame containing COVID-19 case data with countries as rows and time periods as columns.
    It creates a pie chart to visualize the distribution of COVID cases for a specific time period.

    Parameters:
    - dataframe: A pandas DataFrame with countries as rows and time periods as columns.
    - time_period: A specific time period (column) for which the pie chart is to be generated.

    Example Usage:
    plot_pie_chart_covid_cases(covid_df, '2023-11-09')

    The function will display and save a pie chart showing the distribution of COVID cases for the specified time period.

    Note: Make sure to have the 'pandas' and 'matplotlib' libraries installed for this function to work.

    Returns:
    None
    """
    plt.figure(figsize=(8, 8))

    # Extract data for the selected time period
    data_for_time_period = dataframe[time_period]

    # Plotting the pie chart
    plt.pie(data_for_time_period, labels=data_for_time_period.index, autopct='%1.1f%%', startangle=140, colors=['blue', 'red', 'orange'])

    plt.title(f'Distribution of COVID Cases among Countries')

    # Save the figure as an image file (e.g., PNG)
    plt.savefig(f'1.png')

    # Show the plot
    plt.show()

    return

# Read data from Excel file
file_path = r'C:/Users/Administrator/downloads/CovidComparison.xlsx'  # Using a raw string
covid_df = pd.read_excel(file_path, index_col=0)

# Choose a specific time period (e.g., the last one in the DataFrame)
selected_time_period = covid_df.columns[0]

# Call the pie chart function
plot_pie_chart_covid_cases(covid_df, selected_time_period)
