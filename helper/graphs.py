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

def renderGraph(x, y, graph, title):
   df = getData()
   hori = df.iloc[:, [x - 1]]
   verti = df.iloc[:, [y - 1]]
   plt.title(title)   
      
   if graph == 1: plt.plot(hori, verti)
   elif graph == 2: plt.scatter(hori, verti)
   elif graph == 3: plt.hist(hori, verti)
   elif graph == 4: plt.bar(hori, verti)
   else: return ValueError('Invalid Graph!')
   
def customGraph(): 
   ''' Customize Graph '''
   # Show the data and make the user select (2 value)
   # Select the type of graph the user wants (plot, scatter, hist, bar, heat)
   # customize the grapth (title, color, figure, ticks, label)
   print(f'''
      Choose you x axis and y axis
      (1) Year              (7) Vertical_Wind_Shear
      (2) Month             (8)Midlevel_Humidity,
      (3) No. of Typhoons   (9) SeaLevelPressure
      (4) ONI               (10) MJO_Phase
      (5) Nino3.4           (11) Prev_month_typhoons
      (6) West_Pacific_SST                
   ''')
   
   x = int(input('x > ')) 
   y = int(input('y > ')) 
   
   print(f'''
      Choose your graph.
      (1) Line        (3) Hist      
      (2) Scatter     (4) Bar     
   ''')
   
   graph = int(input('Graph > ')) 
   title = input('Title > ')
   renderGraph(x, y, graph, title)
   return title
   