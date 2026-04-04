import matplotlib.pyplot as plt
import pandas as pd

def getData(): 
   return pd.read_csv('./philippines_typhoon_monthly_2014_2024.csv')

def main():
   print("Greetings!")

if __name__ == "__main__":
   main()

