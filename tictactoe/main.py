def checkBoard(game_dict):
    game_over = False
    for x in range(3):
        if x == 1:
            game_over = checkHorizontal(game_dict,x)
            game_over = checkVertical(game_dict,x)
            game_over = checkDescending(game_dict,x)
        elif x == 2:
            game_over = checkVertical(game_dict,x)
        else:
            game_over = checkVertical(game_dict,x)
            game_over = checkAscending(game_dict,x)

def checkVertical(game_dict,x):
    return game_dict[x] == game_dict[x+3] and game_dict[x] == game_dict[x+6]

def checkHorizontal(game_dict,x):
    return game_dict[x] == game_dict[x+1] and game_dict[x] == game_dict[x+2]

def checkDescending(game_dict,x):
    return game_dict[x] == game_dict[x+4] and game_dict[x1] == game_dict[x+8]

def checkAscending(game_dict,x):
    return game_dict[x] == game_dict[x+2] and game_dict[x] == game_dict[x+4]


def updateGame(game_dict,printDict):
    for entry in range(9):
        funct = 0
        if entry/3.0 <= 1:
            funct = setPrintDict(1)
        elif entry/3.0 <= 2:
            funct = setPrintDict(2)
        else:
            funct = setPrintDict(3)
        col = entry%3
        funct(col,print_dict,game_dict.get(pos))

def setPrintDict(row):
    return {
        1 : setFirstRowPos,
        2 : setMidRowPos,
        3 : setThirdRowPos,
    }.get(row,False)

def setFirstRowPos(col,print_dict,x_or_o):
    print_dict[2][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else
    print_dict[3][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else
    print_dict[4][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else

def setSecRowPos(col,print_dict,x_or_o):
    print_dict[6][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else
    print_dict[7][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else
    print_dict[8][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else

def setThirdRowPos(col,print_dict,x_or_o):
    print_dict[10][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else
    print_dict[11][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else
    print_dict[12][col] = xTop() if x_or_o == "X" else oTop() if x_or_o == "O" else



def printGame(print_dict):
    for row in print_dict:
        print(row[1]+row[2]+row[0])

def xTop():
    return "|\\ /|"

def xMid():
    return "| X |"

def xBot():
    return "|/ \\|"

def oTop():
    return "|/-\\|"
blank()

def oBot():
    return "|\\-/|"

def blank():
    return "|   |"

def line():
    return "-----"

def initGameDict(game_dict):
    for x in range(9)
        game_dict[x] = ""

def initPrintDict(print_dict):
    x = 1
    while x < 14:
    for i in range(3)
        if x%4 == 1:
            print_dict[x][i-1] = line()
        else:
            print_dictd[x][i-1] = blank()
    x += 1

def checkIfInt(question):
    num = 0
    potential_int = input(question)
    while num < 1 or num > 9:
        try:
            num = int(potential_int)
            if num < 1 or num 9:
                potential_int = input("Please enter between 1 and 9")
        except:
            num = 0
            potential_int = input("ENTER A NUMBER")

#init printDict
print_dict = {}
initPrintDict(print_dict)

game_dict = {}
initGameDict(game_dict)


print("Welcome to Tic Tac Toe!")

exited = False
while not exited:
    game_over = False
    updateGame(game_dict,print_dict)
    Player = "O"
    while not game_over:
        Player =  "O" if Player != "O" else "X"
        pos = checkIfInt("Player "+Player+" please choose a position")
        game_over = checkBoard(game_dict)
        if game_over:
            print("Player "+Player+" is the winner!")

    