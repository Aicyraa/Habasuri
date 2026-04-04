import matplotlib.pyplot as plt
import pandas as pd
from  .data import getData 

def grph1():
   year, numOfTyph = getData().loc[:, ['Year', 'Number_of_Typhoons']]
   plt.bar(year, year)
   plt.title('Seasonal Patterns')
   
def grph2():
   pass

def grph3():
   pass

def grph4():
   pass