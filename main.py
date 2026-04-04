import matplotlib.pyplot as plt
import pandas as pd
from helper import graphs 

def readyGraph(graph):
   code = -1
   
   match graph:
      case 1:
         graphs.grph1()
         code =   
      case 2:
         pass
      case 3:
         pass
      case 4:
         pass
      case 5:
         pass
      case _:
         code = 'Invalid'
   
   return code

def renderGraph(graph):
   code = readyGraph(graph)
   plt.clf()
   plt.savefig('./image_graph/')
   return code

if __name__ == "__main__": 
   
   while True:
      print(f'''
         What would you like to see today?
            Premade Graph
               (1) Seasonal Patterns
               (2) Yearly Patterns      
               (3) El Nino Impact of typoons      
               (4) Matrix of all numeric columns      
            Customize (5)
            (0) Exit
      ''')

      graphChoice = int(input('> '))
      
      if graphChoice == 0: 
         print('>> Byebye')
         break
      else:
         graphCode = renderGraph(graphChoice)
         print(f'>> {graphCode}')
         print('-'*40)

