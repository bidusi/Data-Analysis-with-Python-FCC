import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')
    print(df)
   
    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    print(f"R-squared: {res.rvalue**2:.6f}")
    m = res.slope
    x = df['Year']
    c = res.intercept
    print(res.intercept,res.slope)
    
    # Create second line of best fit
    r2_years = df.loc[df['Year']>=2000]
    pred_years = pd.Series(np.arange(2014,2051,1))
    new_years = [x,pred_years]
    x = pd.concat(new_years)
    pred_years.describe()
    reg2 = linregress(r2_years['Year'], r2_years['CSIRO Adjusted Sea Level'])
    print(f"R-squared: {reg2.rvalue**2:.6f}")
    m2 = reg2.slope
    c2 = reg2.intercept
    new_years2 = [r2_years['Year'],pred_years]
    x2 = pd.concat(new_years2)
    # Create scatter plot
    fig,ax = plt.subplots()
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(x,m*x+c)
    plt.plot(x2,m2*x2+c2)    
    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()