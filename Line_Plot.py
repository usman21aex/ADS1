# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:20:41 2023
@author: Usman
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_covid_data(dataframe):
    """
    Function to create a line plot for COVID cases and deaths.

    Arguments:
    dataframe -- A pandas DataFrame with time periods as columns and categories as rows.

    This function takes a DataFrame containing COVID-19 data with time periods as columns and categories (e.g., cases and deaths) as rows.
    It creates a line plot to visualize the trends of COVID cases and deaths over time.

    Parameters:
    - dataframe: A pandas DataFrame with time periods as columns and categories as rows.

    Example Usage:
    plot_covid_data(covid_df)

    The function will display and save a line plot showing the trends of COVID cases and deaths in the USA over time.

    Note: Make sure to have the 'pandas' and 'matplotlib' libraries installed for this function to work.

    Returns:
    None
    """
    plt.figure(figsize=(16, 8))

    for category in dataframe.index:
        plt.plot(dataframe.columns, dataframe.loc[category], label=category)

    plt.xlabel('Time Period')
    plt.ylabel('Cases and Deaths')
    plt.title('COVID Cases and Deaths in USA')
    plt.legend()
    plt.grid(True)

    # Save the figure as an image file (e.g., PNG)
    plt.savefig('Covid_in_USA_Line_Plot.png')

    # Show the plot
    plt.show()

    return

# Read data from Excel file
file_path = r'C:/Users/Administrator/downloads/CovidData.xlsx'  # Using a raw string
covid_df = pd.read_excel(file_path, index_col=0)

# Call the plot function
plot_covid_data(covid_df)
