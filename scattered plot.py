# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:08:27 2023

@author: usman
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_scatter_covid_data(dataframe):
    """
    Function to create a scatter plot for COVID cases and deaths.

    Arguments:
    dataframe -- A pandas DataFrame with time periods as columns and categories as rows.
    """
    plt.figure(figsize=(12, 8))

    # Scatter plot for each category
    for category in dataframe.index:
        plt.scatter(dataframe.columns, dataframe.loc[category], label=category, alpha=0.7)

    plt.xlabel('Time Period')
    plt.ylabel('Cases and Deaths')
    plt.title('Scatter Plot of COVID Cases and Deaths in USA')
    plt.legend()
    plt.grid(True)

    # Save the figure as an image file (e.g., PNG)
    plt.savefig('Covid_in_USA_Scatter_Plot.png')

    # Show the plot
    plt.show()

    return

# Read data from Excel file
file_path = r'C:/Users/Administrator/downloads/CovidData.xlsx'  # Using a raw string
covid_df = pd.read_excel(file_path, index_col=0)

# Call the scatter plot function
plot_scatter_covid_data(covid_df)
