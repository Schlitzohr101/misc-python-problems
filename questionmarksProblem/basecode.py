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