import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(filepath_or_buffer='https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/10d2fe8058be34cdf47d730d03e5ee1500bf23cf/fcc-forum-pageviews.csv',index_col='date')
df.describe()

# Clean data
df= df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]
x= df.index.to_numpy(dtype='datetime64[ns]')

def draw_line_plot():
    nx=df.index.to_numpy(dtype='datetime64[ns]')
    # Draw line plot
    fig,ax = plt.subplots(figsize=(12, 3))
    ax.plot(nx,df['value'],color='#d62728',linewidth=1)
    print(nx.shape,df['value'].shape)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
    
draw_line_plot()

df_bar = df.reset_index()
df_bar

df_bar['date'] = pd.to_datetime(df_bar['date'])

df_bar['Month'] = df_bar['date'].dt.month
df_bar['Year'] = df_bar['date'].dt.year
df_bar.head()

pivot_df = df_bar.pivot_table(index='Year', columns='Month', values='value', aggfunc='mean')

pivot_df.fillna(0)

x=pd.Series(pivot_df.index).index
width = 1/(len(pivot_df.columns)*2)
width

def draw_bar_plot():
  fig,ax = plt.subplots()
  multiplier = 0
  for a in pivot_df.columns:
    offset=width*multiplier
    ax.bar(x+offset,pivot_df[a],width=width)
    multiplier+=1
  plt.xlabel('Years')
  plt.ylabel('Average Page Views')
  ax.set_xticks(x + width, pivot_df.index)
  ax.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], loc='upper left', ncols=1)
  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

draw_bar_plot()

pivot_df_year = df_bar.pivot_table(index='Year', columns='Month', values='value', aggfunc='mean')

df.index

df.index = pd.to_datetime(df.index)
df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]

def draw_box_plot():
  fig,axs = plt.subplots(1, 2, figsize=(20,5))
  sns.boxplot(data=df_box, x='year', y='value', palette="tab10", hue=None, ax=axs[0],flierprops={"marker": "|"})
  axs[0].set_title('Year-wise Box Plot (Trend)')
  axs[0].set_ylabel('Page Views')
  axs[0].set_xlabel('Year')
  sns.boxplot(data=df_box, x='month', y='value', palette="husl", hue=None, ax=axs[1],flierprops={"marker": "|"})
  axs[1].set_title('Month-wise Box Plot (Seasonality)')
  axs[1].set_ylabel('Page Views')
  axs[1].set_xlabel('Month')
  axs[1].set_xticks(range(12))  # Set the tick positions
  axs[1].set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])  # Set the tick labels
  plt.subplots_adjust(left=0.2, right=0.8, bottom=0.2, top=0.8, wspace=0.2)
 # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig

draw_box_plot()

