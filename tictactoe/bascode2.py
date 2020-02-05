#HOW DO YOU DO FELLOW FELLOW CHILDREN
#remember we start from 1 and go to 9
#evey multiple of 3 marks the end of a line
#start from the top and 
def checkBoard(game_dict):
    game_over = False
    game_over = checkHorizontal(game_dict,1) if not game_over else True
    game_over = checkVertical(game_dict,1) if not game_over else True
    game_over = checkDescending(game_dict,1) if not game_over else True
    game_over = checkVertical(game_dict,2) if not game_over else True
    game_over = checkVertical(game_dict,3) if not game_over else True
    game_over = checkAscending(game_dict,3) if not game_over else True
    game_over = checkHorizontal(game_dict,4) if not game_over else True
    game_over = checkHorizontal(game_dict,7) if not game_over else True
    return game_over  

#free of charge
def checkVertical(game_dict,x):
    return game_dict[x] == game_dict[x+3] and game_dict[x] == game_dict[x+6] if not game_dict[x] == "" else False

def checkHorizontal(game_dict,x):
    return game_dict[x] == game_dict[x+1] and game_dict[x] == game_dict[x+2] if not game_dict[x] == "" else False

def checkDescending(game_dict,x):
    return game_dict[x] == game_dict[x+4] and game_dict[x+1] == game_dict[x+8] if not game_dict[x] == "" else False

def checkAscending(game_dict,x):
    return game_dict[x] == game_dict[x+2] and game_dict[x] == game_dict[x+4] if not game_dict[x] == "" else False
#

#need to write this
def updateGame(game_dict,printDict):
  #so looks complex but lets deconstruct this
  #we have to change the entire block in the print dictionary
  #based on what is in the game dictionary
  #the deciding factor is the game_dict as it controls what is
  #what
  #so lets loop through it
  #first the rows
  for row in range(3): #row goes from 0-2
    #then the columns
    for col in range(3): #col goes from 0-2
      #now we have this thing called a closure,
      #it takes a int and gives back a setRowPos function
      #meaning it will write a block in the print_dict
      #lets do that here
      funct = setPrintDict(0000+0000) #row from 1 - 3
      #so the entry goes from 1-9
      #row from 0-2, and same from col
      #col resets every row
      #need to make a expression to get 1-9
      entry = ((0000) * 0000) + (0000+0000)
      #this is the biggest hint
      #the function call, this could be any of the three listed below
      funct(col,print_dict,game_dict.get(entry))

#this is the closure
#take note of the function names used and how the dont have ()
#consider print, to use print(), to reference just print
#same principal here. Based on the key, in this case 1,2,3,
#a function reference is returned. Same as one could return a 
#stirng or a int.
def setPrintDict(row):
    return {
        1 : setFirstRowPos,
        2 : setSecRowPos,
        3 : setThirdRowPos,
    }.get(row,False)

def setFirstRowPos(col,print_dict,x_or_o):
    print_dict[2][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else blank()
    print_dict[3][col] = xMid() if x_or_o == "X" else oMid() if x_or_o == "O" else blank()
    print_dict[4][col] = xBot() if x_or_o == "X" else oBot() if x_or_o == "O" else blank()

def setSecRowPos(col,print_dict,x_or_o):
    print_dict[6][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else blank()
    print_dict[7][col] = xMid() if x_or_o == "X" else oMid() if x_or_o == "O" else blank()
    print_dict[8][col] = xBot() if x_or_o == "X" else oBot() if x_or_o == "O" else blank()

def setThirdRowPos(col,print_dict,x_or_o):
    print_dict[10][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else blank()
    print_dict[11][col] = xMid() if x_or_o == "X" else oMid() if x_or_o == "O" else blank()
    print_dict[12][col] = xBot() if x_or_o == "X" else oBot() if x_or_o == "O" else blank()



def printGame(print_dict):
    x = 1
    while x < 14:
        print(print_dict[x][0]+print_dict[x][1]+print_dict[x][2])
        x+=1

def xTop():
    return "|\\ /|"

def xMid():
    return "| X |"

def xBot():
    return "|/ \\|"

def oTop():
    return "|/-\\|"

def oMid():
    return "|| ||"

def oBot():
    return "|\\-/|"

def blank():
    return "|   |"

def line():
    return "-----"

#set each of the entries to ""
def initGameDict(game_dict):
    for x in range(9):
        game_dict[x+1] = ""

#here the work is a bit more complicated
#we want each entry to be each line we have to print
#thats 14 lines, for 9 3x3 blocks with bordes on the top and
#bottom
def initPrintDict(print_dict):
    x = 1
    while x < 14:
      #so for each line create a list of 3 blank strings
      print_dict[x] = ["","",""]
      #for each blank string in the list
      for i in range(3):
        #if the line to be printed is a multiple of 4 plus 1
        if x%4 == 1:
          #set the string to be a line()
          print_dict[x][i] = 0000
        else:
          #set the string to be a blank()
          print_dict[x][i] = 0000
      x += 1

#ask me about this
def checkIfInt(question):
    num = 0
    potential_int = input(question)
    while num < 1 or num > 9:
        try:
            num = int(potential_int)
            if num < 1 or num > 9:
                potential_int = input("Please enter between 1 and 9: ")
        except:
            num = 0
            potential_int = input("ENTER A NUMBER: ")
    return num
    

print_dict = {}
initPrintDict(print_dict)

game_dict = {}
initGameDict(game_dict)

printGame(print_dict)

print("Welcome to Tic Tac Toe!")

#is the game exited before we even start? set to answer
exited = 0000
while not exited:
    #here we start the game, so the game_over should be false
    game_over = 0000
    updateGame(0000,0000)
    #look down to see why Player starts at O
    Player = "O"
    #game wont stop if we don't make sure the 
    turn = 0
    while not game_over:
        Player =  "O" if Player != "O" else "X"
        pos = checkIfInt("Player "+Player+" please choose a position: ")
        while not game_dict[pos] == "":
            pos = checkIfInt("Choose a position that isnt populated: ")
        game_dict[pos] = Player
        updateGame(game_dict,print_dict)
        game_over = checkBoard(game_dict)
        if game_over and turn < 9:
            printGame(print_dict)
            print("Player "+Player+" is the winner!")
        elif not game_over and turn > 9:
            printGame(print_dict)
            print("TIE GAME NO WINNER")
        else:    
            
            printGame(print_dict)
            turn += 1
    answer = input("Would you like to Play again? ")
    answer = answer.upper()
    while answer[0] != "Y" and answer[0] != "N":
        answer = input("Enter yes or no: ")
        answer = answer.upper()
    if answer[0] == "N":
        exited = True
print("shutting down...")
