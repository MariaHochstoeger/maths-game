import random

print("Welcome to the Maths Game!")
print("Here you can test your knowledge in maths.")
print("You can choose which mathematical operation you would like to practice.")
print("You will play 5 rounds. Then you get your score.")
print("Let's start!\n")

def get_username():
    """
    Ask user for their username.
    Validate the input to not be empty and return a welcome message 
    with the username to the console.
    """
    username = ""
    username = input("Please enter your name: \n").strip()

    while username == "":
        username = input("You did not enter anything. Please enter a valid name: \n")

    print(f"\nHello {username}!")
    return username

def choose_operation():
    """
    Ask the user to choose which mathematical equations they want to practice.
    Validate the user input.
    """
    print("\nChoose the type of mathematical operator you would like to play with.")
    print("You can choose from: add, subtract, multiply, divide")
    print("If you choose add, subtract or multiply you need to give your answers as integers, e.g. 1 or -5")
    print("If you choose divide, you need to give your answer as a float with one decimal place, e.g. 2.3 or 3.1")
    operators = ['add', 'subtract', 'multiply', 'divide']
    chosen_operator = ""
    chosen_operator = input("\nPlease enter your chosen mathematical operator: \n").lower()
    
    while chosen_operator not in operators:
        print(f"'{chosen_operator}' is not a valid input.")
        chosen_operator = input(f"Please choose one of the operators {operators}: \n").lower()

    return chosen_operator
    
def display_question(ops):
    """
    Generate a mathematical operation to be solved
    based on the user's selection of the operator.
    Validate user input and generate appropriate feedback.
    Ask 5 questions in a row and keep score of correct answers.
    """
    correct_score = 0
    i = 0
    
    while i < 5:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)

        if ops == 'add':
            calculated_result = num1 + num2
            while True: # repeat question until a valid answer is provided
                try:
                    given_result = int(input(f"\nQuestion: {num1} + {num2} = \n"))
                    break # exit loop once there is a valid integer provided
                except ValueError as e:
                    print(f"Caught an error: {e}")
                    print("Please provide a number without any decimals, e.g. 3")

            if calculated_result == given_result:
                correct_score += 1
                print("That is correct!")
            else:
                print("Oh no, that is incorrect... ")
            i += 1
            
        if ops == 'subtract':
            calculated_result = num1 - num2
            while True: # repeat question until a valid answer is provided
                try:
                    given_result = int(input(f"\nQuestion: {num1} - {num2} = \n"))
                    break # exit loop once there is a valid integer provided
                except ValueError as e:
                    print(f"Caught an error: {e}")
                    print("Please provide a number without any decimals, e.g. 3, -2")
            if calculated_result == given_result:
                correct_score += 1
                print("That is correct!")
            else:
                print("Oh no, that is incorrect... ")
            i += 1

        if ops == 'multiply':
            calculated_result = num1 * num2
            while True: # repeat question until a valid answer is provided
                try:
                    given_result = int(input(f"\nQuestion: {num1} * {num2} = \n"))
                    break # exit loop once there is a valid integer provided
                except ValueError as e:
                    print(f"Caught an error: {e}")
                    print("Please provide a number without any decimals, e.g. 3")
            if calculated_result == given_result:
                correct_score += 1
                print("That is correct!")
            else:
                print("Oh no, that is incorrect... ")
            i += 1    

        if ops == 'divide':
            #Ensure that numerator is larger than denominator
            if num1 < num2:
                num1, num2 = num2, num1
            calculated_result = round(num1 / num2, 1)
            while True: # repeat question until a valid answer is provided
                try:
                    given_result = round(float(input(f"\nQuestion: {num1} / {num2} = \n")), 1)
                    break # exit loop once there is a valid float is provided
                except ValueError as e:
                    print(f"Caught an error: {e}")
                    print("Please provide a number as an answer.")
                    print("Your answer will be rounded to 1 decimal place.")
            if calculated_result == given_result:
                correct_score += 1
                print("That is correct!")
            else:
                print("Oh no, that is incorrect... ")
            i += 1    
     
    return correct_score

def display_score(score):
    if score == 0:
        print(f"\nOH NO! You got {score} correct.")
    elif score == 5:
        print(f"\nCONGRATULATIONS! You aced it and you got {score} correct.")
    else:
        print(f"\nWell done. You got {score} correct.")

def end_of_game():
    print("\nIf you would like to play again, enter y.")
    print("If you would not like to play again, enter n.")
    while True:
        play_again = input("Would you like to play again? \n").lower()
        if play_again == "y":
            chosen_operator = choose_operation()
            correct_score = display_question(chosen_operator)
            display_score(correct_score)
            end_of_game()
            break
        elif play_again == "n":
            break
        else:
            print("Please provide a valid input, y or n.")
        

if __name__ == "__main__":
    username = get_username()
    chosen_operator = choose_operation()
    correct_score = display_question(chosen_operator)
    display_score(correct_score)
    end_of_game()