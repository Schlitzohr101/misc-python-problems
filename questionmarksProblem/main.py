def isNum(num):
  return {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
  }.get(num, False)

def QuestionsMarks(str):
  question_count = 0
  first_num  = -1
  second_num = -1
  total = -1
  answer = "false"
  for i in range(len(str)):
    #print(i)
    #print(" "+str[i])
    if isNum(str[i]):
      if first_num == -1:
        first_num = int(str[i])
        #print("first_num = ",first_num)
      elif second_num == -1:
        second_num = int(str[i])
        #print("second_num = ",second_num)
        total = first_num + second_num
        #print("total = ",total)
        if total != 10 and question_count < 3:
          #print("reset vars")
          first_num  = -1
          second_num = -1
          total = -1
          question_count = 0
        else:
          answer = "true"
    elif str[i] == '?':
      question_count += 1
  return answer
        
our_input = "acc?7??sss?3rr1??????5"
if (QuestionsMarks(our_input) != "true"):
    print("result: "+QuestionsMarks(our_input))
    print("incorrect output for "+our_input)
    print("expected output = /'false/'")
else:
    print("Correct! nice job")

our_input = "aa6?9"
if (QuestionsMarks(our_input) != "false"):
    print("result: "+QuestionsMarks(our_input))
    print("incorrect output for "+our_input)
    print("expected output = /'false/'")
else:
    print("Correct! nice job")