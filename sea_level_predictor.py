import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    return fig

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(df['Year'].min(), 2051))
    sea_levels = res.intercept + res.slope * years
    ax.plot(years, sea_levels)

    # Create second line of best fit

    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = res_recent.intercept + res_recent.slope * years_recent

    ax.plot(years_recent, sea_levels_recent)

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()