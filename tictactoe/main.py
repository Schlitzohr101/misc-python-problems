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

def checkVertical(game_dict,x):
    return game_dict[x] == game_dict[x+3] and game_dict[x] == game_dict[x+6] if not game_dict[x] == "" else False

def checkHorizontal(game_dict,x):
    return game_dict[x] == game_dict[x+1] and game_dict[x] == game_dict[x+2] if not game_dict[x] == "" else False

def checkDescending(game_dict,x):
    return game_dict[x] == game_dict[x+4] and game_dict[x] == game_dict[x+8] if not game_dict[x] == "" else False

def checkAscending(game_dict,x):
    return game_dict[x] == game_dict[x+2] and game_dict[x] == game_dict[x+4] if not game_dict[x] == "" else False


def updateGame(game_dict,printDict):
    for row in range(3):
        for col in range(3):
            funct = setPrintDict(row+1)
            entry = ((row) * 3) + (col+1)
            #print("entry: ",entry)
            funct(col,print_dict,game_dict.get(entry))

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

def initGameDict(game_dict):
    for x in range(9):
        game_dict[x+1] = ""

def initPrintDict(print_dict):
    x = 1
    while x < 14:
      print("on x :",x)
      print_dict[x] = ["","",""]
      for i in range(3):
        print("for i:",i)
        if x%4 == 1:
          print("set as line")
          print_dict[x][i] = line()
        else:
          print("set as blank")
          print_dict[x][i] = blank()
      x += 1

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
    

#init printDict
print_dict = {}
initPrintDict(print_dict)

game_dict = {}
initGameDict(game_dict)

print(game_dict)
printGame(print_dict)

print("Welcome to Tic Tac Toe!")

exited = False
while not exited:
    game_over = False
    updateGame(game_dict,print_dict)
    Player = "O"
    turn = 0
    while not game_over:
        Player =  "O" if Player != "O" else "X"
        pos = checkIfInt("Player "+Player+" please choose a position: ")
        while not game_dict[pos] == "":
            pos = checkIfInt("Choose a position that isnt populated: ")
        game_dict[pos] = Player
        updateGame(game_dict,print_dict)
        game_over = checkBoard(game_dict)
        if game_over:
            printGame(print_dict)
            print("Player "+Player+" is the winner!")
        elif turn > 9:
            printGame(print_dict)
            print("TIE GAME NO WINNER")
            game_over = True
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
