import random
import time
import shutil

terminal_width = shutil.get_terminal_size().columns
operators = ['+', '-','*']
min_num = 3
max_num = 34


def terminalprint():
    print("-" * terminal_width)


def padding(msg):
    pad = (terminal_width - len(msg))//2
    return pad


def generator():
    operand1 = random.randint(min_num, max_num)
    operand2 = random.randint(min_num, max_num)
    operator = random.choice(operators)
    expression = str(operand1) + " " + operator + " " + str(operand2)
    answer = eval(expression)
    return expression, answer


terminalprint()
msg = "Timed Maths Quiz"
print(" " * padding(msg), msg)


while True:
    terminalprint()
    msg = "Press 'Enter' to start"
    print(" " * padding(msg), msg)
    terminalprint()
    input()
    start_time = time.time()
    correct = 0
    wrong = 0
    for i in range(1, 11):
        expression, answer = generator()
        user_input = input("Quesiton #"+str(i)+": "+expression+" = ")
        try:
            user_input = int(user_input)
        except Exception:
            pass
        else:
            if user_input == answer:
                correct += 1
            else:
                wrong += 1
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print("Correct answers: ", correct, "\nWrong answers: ", wrong, "\nTime taken to answer: ", total_time, " seconds.")
    user_choice = input("Enter 0 to quit\nPress 'Enter' to continue:\t\t")
    if user_choice == 0:
        break
