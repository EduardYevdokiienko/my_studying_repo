try:
    question_1 = int(input("How many test cases you execute per dey: "))
    if question_1 > 0:
        print("You can do more!")
    elif question_1 > 10:
        print("Well done!")
    else:
        print("Incorrect input! Try to improve your result!")
except ValueError:
    print("Invalid input!")
