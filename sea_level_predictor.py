import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)

    # Create first line of best fit (using all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res_all.intercept + res_all.slope * x_pred1
    plt.plot(x_pred1, y_pred1, 'r', label='Fit: All Data')

    # Create second line of best fit (from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res_recent.intercept + res_recent.slope * x_pred2
    plt.plot(x_pred2, y_pred2, 'g', label='Fit: From 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
