import matplotlib.pyplot as plt
import pandas as pd
from helper import graphs 

def readyGraph(graph):
   match graph:
      case 1:
         graphs.grph1()
         return graph
      case 2:
         graphs.grph2()
         return graph
      case 3:
         graphs.grph3()
         return graph
      case 4:
         graphs.grph4()
         return graph
      case 5:
         return graphs.customGraph()

def renderGraph(graph):
   code = readyGraph(graph)
   plt.savefig(f'./image_graph/graph_{code}.png')
   plt.close()

if __name__ == "__main__":
   while True:
      print(f'''
         What would you like to see today?
            Premade Graph
               (1) Seasonal Patterns
               (2) Yearly Patterns      
               (3) El Nino Impact of typoons      
               (4) Matrix of all numeric columns      
            (5) Customize 
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