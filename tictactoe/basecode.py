def checkBoard(game_dict):
    game_over = False
    for x in range(3):
        if x == 1:
            game_over = 0000
            game_over = 0000
            game_over = 0000
        elif x == 2:
            game_over = 0000
        else:
            game_over = 0000
            game_over = 0000

def updateGame(game_dict,printDict):
    for entry in range(9):
        funct = 0
        if entry/3.0 <= 1:
            funct = setPrintDict(0000)
        elif entry/3.0 <= 2:
            funct = setPrintDict(0000)
        else:
            funct = setPrintDict(0000)
        col = entry%3
        funct(col,print_dict,game_dict.get(pos))

def setPrintDict(row):
    return {
        1 : 0000,
        2 : 0000,
        3 : 0000,
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
        print(row[0000]+row[0000]+row[0000])

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
    for x in range(9)
        game_dict[x] = 0000

def initPrintDict(print_dict):
    x = 1
    while x < 14:
    for i in range(3)
        if x%4 == 1:
            print_dict[x][i-1] = 0000
        else:
            print_dictd[x][i-1] = 0000
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

