import matplotlib.pyplot as plt
from helper import graphs 

def readyGraph(graph):
   code = 'Invalid'
   
   match graph:
      case 1:
         graphs.grph1()
         code = 'Success'  
      case 2:
         graphs.grph2()
         code = 'Success'  
      case 3:
         graphs.grph3()
         code = 'Success'
      case 4:
         graphs.grph4()
         code = 'Success'  
      case 5:
         code = 'Success'  
   return code

def renderGraph(graph):
   code = readyGraph(graph)
   plt.savefig(f'./image_graph/graph_{graph}.png')
   plt.close()
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

