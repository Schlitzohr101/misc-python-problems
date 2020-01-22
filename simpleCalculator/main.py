import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return 'operation not allowed'
    else:
        return a/b

def exp(a,b):
    return math.pow(a,b)

def getOperation(c):
    return {
        '+' : add,
        '-' : sub,
        '*' : mult,
        '/' : div,
        '^' : exp,
    }.get(c,False)

print("Calculator ready")
print("Enter expressions or enter \'q\' to exit")

operator = ""
expression = ""
exited = False
last_index = 0

while not exited:
    first_num = ""
    second_num = ""
    last_index = 0
    end_index = 0
    num_len = 1000000000
    expression = input(":")
    for i in range(len(expression)):
        print(expression[i])
        if not expression[i].isdigit() and not expression[i].isspace():
            if expression[i] == "-" and expression[i+1].isdigit():
                last_index = i
                print("last index set")
            else:
                if expression[i] == 'q':
                    operator = expression[i]
                    print("operator: "+operator)    
                else:
                    operator = expression[i]
                    print("operator: "+operator)
                    if first_num == "":
                        first_num = int(expression[last_index:i])
                        print("first_num: ",first_num)
                        print("last index set")
                    else:
                        last_index = i
        elif expression[i].isspace():
            if first_num == "":
                first_num = int(expression[last_index:i-1])
                print(first_num)
                print("last index set")
            elif operator != "":
                last_index = i
        else:
           if last_index+num_len < i
    i = len(expression)
    # while not expression[i].isspace():
    #     i-=1
    if operator == "q":
            exited = True
    else:
        second_num = int(expression[last_index:i])
        print("second_num: ",second_num)
        if getOperation(operator):
            operation = getOperation(operator)
            print("final: ",operation(first_num,second_num))
        else:
            print("Error could not parse expression")
print("shutting down...")
            

