import os

dir = os.path.dirname(__file__)
pokelistf = open(os.path.join(dir, 'numberlist.txt'), 'r')
statlistf = open(os.path.join(dir,'statlist.txt'), 'r')
   
pokelist = []
for line in pokelistf:
   pokelist.append(line.replace('\n', ''))
   
statlist = []
for line in statlistf:
   statlist.append(line.replace('\n', ''))
      
kill = False
      
while True: 
   bluepokes = []
   bluepokes.append(input('Input 1st blue Pokemon: '))
   bluepokes.append(input('Input 2nd blue Pokemon: '))
   bluepokes.append(input('Input 3rd blue Pokemon: '))
      
   redpokes = []
   redpokes.append(input('Input 1st red Pokemon: '))
   redpokes.append(input('Input 2nd red Pokemon: '))
   redpokes.append(input('Input 3rd red Pokemon: '))
   
   print('\n')
   print('Special types:  FIR WTR ELE GRS ICE PSY DRG DRK')
   print('Physical types: NML FGT PSN GRN FLY BUG RCK GHO STL')
   
   
   blueheader = 'BLUE'
   redheader = 'RED'

   print(blueheader.rjust(34), '|', redheader.ljust(34))
   print('           HP  Atk Def SpA SpD Spe | HP Atk Def SpA SpD Spe')
 
   for x in range(0, 3):
      bluedexnum = -1
      reddexnum = -1
     
      try: 
         bluedexnum = pokelist.index(bluepokes[x])
         reddexnum = pokelist.index(redpokes[x])
      except:
         print('Whatever you just entered, it contained something that is not the name of a Pokemon in Stadium 2.')
         break
      
      print(bluepokes[x].ljust(10), statlist[bluedexnum], '|', statlist[reddexnum], redpokes[x].rjust(10))
         
   print('\n')
     
   throwaway = input('Type exit to quit, or hit enter to prepare for next match.')
   if throwaway == "exit":
      break
   print('\n')