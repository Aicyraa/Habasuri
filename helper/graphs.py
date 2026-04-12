import matplotlib.pyplot as plt
import pandas as pd
from  .data import getData 

def grph1():
   """Seasonal Patterns - Average typhoons per month across all years"""
   df = getData()
   monthly_avg = df.groupby('Month')['Number_of_Typhoons'].mean()

   plt.figure(figsize=(10, 6))
   plt.bar(monthly_avg.index, monthly_avg.values, color='steelblue')
   plt.xlabel('Month')
   plt.ylabel('Average Number of Typhoons')
   plt.title('Seasonal Patterns - Monthly Typhoon Averages (2014-2024)')
   plt.xticks(range(1, 13))
   return plt
   
def grph2():
   """Yearly Patterns - Total typhoons per year"""
   df = getData()
   yearly_total = df.groupby('Year')['Number_of_Typhoons'].sum()

   plt.figure(figsize=(10, 6))
   plt.bar(yearly_total.index, yearly_total.values, color='coral')
   plt.xlabel('Year')
   plt.ylabel('Total Number of Typhoons')
   plt.title('Yearly Patterns - Typhoon Count per Year (2014-2024)')
   plt.xticks(yearly_total.index)
   return plt
   
def grph3():
   """El Nino Impact - Scatter plot of ENSO vs typhoon frequency"""
   df = getData()

   plt.figure(figsize=(10, 6))   
   plt.scatter(df['Nino3.4_SST_anomaly'], df['Number_of_Typhoons'], color='darkgreen', alpha=0.7, s=df['Number_of_Typhoons']*30)
   plt.xlabel('Nino3.4 SST Anomaly (°C)')
   plt.ylabel('Number of Typhoons')
   plt.title('El Niño Impact on Typhoon Frequency (2014-2024)')
   plt.axvline(x=0, color='red', linestyle='--', alpha=0.5, label='ENSO Neutral')
   plt.legend()
   plt.grid(True, alpha=0.3)
   return plt
   
def grph4():
   """Correlation Matrix - Heatmap of all numeric columns"""
   df = getData()
   corr = df.corr(numeric_only=True)

   plt.figure(figsize=(12, 10))
   plt.imshow(corr, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
   plt.colorbar(label='Correlation')
   plt.title('Correlation Matrix - Typhoon Data (2014-2024)')

   # Add labels
   labels = corr.columns
   plt.xticks(range(len(labels)), labels, rotation=45, ha='right')
   plt.yticks(range(len(labels)), labels)

   # Add correlation values
   for i in range(len(corr)):
      for j in range(len(corr)):
         plt.text(j, i, f'{corr.iloc[i, j]:.2f}', ha='center', va='center', fontsize=8)

   plt.tight_layout()
   return plt

# Customize Graph Section

DATA_COLUMNS = [
   (1, 'Year'),
   (2, 'Month'),
   (3, 'No. of Typhoons'),
   (4, 'ONI'),
   (5, 'Nino3.4'),
   (6, 'West_Pacific_SST'),
   (7, 'Vertical_Wind_Shear'),
   (8, 'Midlevel_Humidity'),
   (9, 'SeaLevelPressure'),
   (10, 'MJO_Phase'),
   (11, 'Prev_month_typhoons')
]

GRAPH_TYPES = {
   1: ('line', 'Line'),
   2: ('scatter', 'Scatter'),
   3: ('bar', 'Bar'),
   4: ('hist', 'Histogram')
}

COLOR_OPTIONS = [
   (1, 'steelblue'),
   (2, 'coral'),
   (3, 'darkgreen'),
   (4, 'crimson'),
   (5, 'purple'),
   (6, 'orange'),
   (7, 'teal'),
   (8, 'navy'),
   (9, 'maroon'),
   (10, 'olive')
]

def renderGraph(x, y, graph_type, title, color='steelblue', figsize=(10, 6),
                xlabel=None, ylabel=None, xticks=None, yticks=None, grid=False):
   """Render a customizable graph with user-specified options."""
   df = getData()
   x_col = df.columns[x - 1]
   y_col = df.columns[y - 1]
   hori = df[x_col]
   verti = df[y_col]

   plt.figure(figsize=figsize)

   if graph_type == 'line':
      plt.plot(hori, verti, color=color, linewidth=2)
   elif graph_type == 'scatter':
      plt.scatter(hori, verti, color=color, alpha=0.7, s=50)
   elif graph_type == 'bar':
      plt.bar(hori.astype(str), verti, color=color)
   elif graph_type == 'hist':
      plt.hist(verti, bins=10, color=color, edgecolor='black')
   else:
      raise ValueError(f'Invalid graph type: {graph_type}')

   plt.title(title, fontsize=14, fontweight='bold')
   plt.xlabel(xlabel or x_col, fontsize=11)
   plt.ylabel(ylabel or y_col, fontsize=11)

   if xticks:
      plt.xticks(xticks)
   if yticks:
      plt.yticks(yticks)
   if grid:
      plt.grid(True, alpha=0.3)

   plt.tight_layout()
   return plt

def customGraph():
   '''Create a fully customizable graph with user-specified options.'''

   # Step 1: Select X and Y axis
   print('\n' + '='*50)
   print('SELECT X AND Y AXIS')
   print('='*50)
   for i, (num, name) in enumerate(DATA_COLUMNS):
      if i % 2 == 0:
         print(f'   ({num}) {name:<25}', end='')
      else:
         print(f'({num}) {name}')
   print()

   x = int(input('X-axis column (1-11) > '))
   y = int(input('Y-axis column (1-11) > '))

   # Step 2: Select graph type
   print('\n' + '='*50)
   print('SELECT GRAPH TYPE')
   print('='*50)
   for num, (key, name) in GRAPH_TYPES.items():
      print(f'   ({num}) {name}')
   print()

   graph_choice = int(input('Graph type (1-4) > '))
   graph_type = GRAPH_TYPES.get(graph_choice, ('line', 'Line'))[0]

   # Step 3: Select color
   print('\n' + '='*50)
   print('SELECT COLOR')
   print('='*50)
   for num, color in COLOR_OPTIONS:
      print(f'   ({num}) {color}')
   print('   (0) Custom (enter hex/name)')
   print()

   color_choice = int(input('Color (0-10) > '))
   if color_choice == 0:
      color = input('Enter color name or hex code > ')
   else:
      color = COLOR_OPTIONS[color_choice - 1][1]

   # Step 4: Customize title and labels
   print('\n' + '='*50)
   print('TITLE AND LABELS')
   print('='*50)
   title = input(f'Graph title [default: "{DATA_COLUMNS[x-1][1]} vs {DATA_COLUMNS[y-1][1]}"] > ')
   if not title:
      title = f'{DATA_COLUMNS[x-1][1]} vs {DATA_COLUMNS[y-1][1]}'

   xlabel = input(f'X-axis label [default: {DATA_COLUMNS[x-1][1]}] > ')
   ylabel = input(f'Y-axis label [default: {DATA_COLUMNS[y-1][1]}] > ')

   # Step 5: Advanced options
   print('\n' + '='*50)
   print('ADVANCED OPTIONS')
   print('='*50)

   figsize_input = input('Figure size (width,height) [default: 10,6] > ')
   if figsize_input:
      try:
         figsize = tuple(map(int, figsize_input.split(',')))
      except ValueError:
         figsize = (10, 6)
   else:
      figsize = (10, 6)

   grid_input = input('Show grid? (y/n) [default: n] > ').lower()
   grid = grid_input == 'y'

   xticks_input = input('Custom X-ticks (comma-separated, optional) > ')
   xticks = [int(v.strip()) for v in xticks_input.split(',')] if xticks_input else None

   yticks_input = input('Custom Y-ticks (comma-separated, optional) > ')
   yticks = [int(v.strip()) for v in yticks_input.split(',')] if yticks_input else None

   # Render the graph
   renderGraph(x, y, graph_type, title, color, figsize, xlabel, ylabel, xticks, yticks, grid)

   return title
   