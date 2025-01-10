import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    plt.figure(figsize=(7, 6))
    plt.plot(x, y, "o", markersize=2)

    # Create first line of best fit
    res1 = linregress(x, y)
    x_2050 = x.to_list().copy()
    x_2050.extend([year for year in range(2014, 2051)])
    x_2050 = pd.Series(x_2050)

    plt.plot(x_2050, res1.intercept + res1.slope * x_2050, color="r")

    # Create second line of best fit
    x_2000 = x[x > 1999]
    start = x_2000.index[0]
    res2 = linregress(x_2000, y.iloc[start:])
    
    plt.plot(x_2050[x_2050 > 1999], res2.intercept + res2.slope * x_2050[x_2050 > 1999], color="g")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()