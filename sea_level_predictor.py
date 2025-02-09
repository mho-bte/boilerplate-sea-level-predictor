import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], s=10)


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    line_x = range(1880, 2051)
    line_y = slope * line_x + intercept
    plt.plot(line_x, line_y, 'r', label='fit line 1880-2050')


    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    line_x2 = range(2000, 2051)
    line_y2 = slope * line_x2 + intercept
    plt.plot(line_x2, line_y2, 'g', label='fit line 2000-2050')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(loc='upper left')

    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()