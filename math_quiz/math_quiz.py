import random

#This function selects random integer
def integerSelector(first_int, last_int):
    """
    Random integer.
    """
    return random.randint(first_int, last_int)

#this function randomly selects the mathematical Operator
def operatorSelector():
    return random.choice(['+', '-', '*'])

#this function performs a mathematical operation on randomly selected numbers
def calculator(number1, number2, opt):
    exp = f"{number1} {opt} {number2}"
    if opt == '+': 
        ans = number1 + number2
    elif opt == '-': 
        ans = number1 - number2
    else: 
        ans = number1 * number2
    return exp, ans

def math_quiz():
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = integerSelector(1, 10); n2 = integerSelector(1, 5); o = operatorSelector()

        PROBLEM, ANSWER = calculator(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        

        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Restart the loop

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

# if __name__ == "__main__":
#     math_quiz()
