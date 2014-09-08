import os

#get absolute path to input files
dir = os.path.dirname(__file__)
pokelistf = open(os.path.join(dir, 'pokelist.txt'), 'r')
statlistf = open(os.path.join(dir,'statlist.txt'), 'r')
   
pokelist = []
for line in pokelistf:
   pokelist.append(line.replace('\n', ''))  #stripping newline off EOL before adding to list
   
statlist = []
for line in statlistf:
   statlist.append(line.replace('\n', ''))  #stripping newline off EOL before adding to list
   
print('Welcome to StadiumStats, as used in Pixley Commentates Twitch!\n')
    
while True:
   print('For the following inputs, please list one Pokemon at a time.')
   print('Please check spelling.  The stream has them written for you.')
   print('Names must have the first letter capitalized.')
   print('Just in case, these are the valid forms for the following Pokemon:')
   print("  Nidoran-F, Nidoran-M, Farfetch'd, Mr. Mime, Porygon2\n")
   bluepokes = []
   bluepokes.append(input('Input 1st blue Pokemon: '))
   bluepokes.append(input('Input 2nd blue Pokemon: '))
   bluepokes.append(input('Input 3rd blue Pokemon: '))
      
   redpokes = []
   redpokes.append(input('Input 1st red Pokemon:  '))
   redpokes.append(input('Input 2nd red Pokemon:  '))
   redpokes.append(input('Input 3rd red Pokemon:  '))
   
   print('\n')
   #Print out type classification, for reference
   print('Special types:  FIR WTR ELE GRS ICE PSY DRG DRK')
   print('Physical types: NML FGT PSN GRN FLY BUG RCK GHO STL')
   
   print('\n')
   
   print('BLUE'.rjust(34), '|', 'RED'.ljust(34))
   print('           HP  Atk Def SpA SpD Spe | HP Atk Def SpA SpD Spe')
 
   #Python's weird.  The range is inclusive for the first value, but exclusive for the second
   for x in range(0, 3):
      bluedexnum = -1
      reddexnum = -1
     
      try: 
         bluedexnum = pokelist.index(bluepokes[x])
         reddexnum = pokelist.index(redpokes[x])
      except:
         #User gave invalid input
         print('Whatever you just entered, it contained something that is not the name of a Pokemon in Stadium 2.')
         break
      
      #Main part of table
      print(bluepokes[x].rjust(10), statlist[bluedexnum], '|', statlist[reddexnum], redpokes[x].ljust(10))
         
   print('\n')
     
   throwaway = input('Type exit to quit, or hit enter to prepare for next match. ')
   if throwaway == "exit":
      break
   print('\n')