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
    username = input("Please enter your name: ").strip()

    while username == "":
        username = input("You did not enter anything. Please enter a valid name: ")

    print(f"\nHello {username}!\n")
    return username

def choose_operation():
    """
    Ask the user to choose which mathematical equations they want to practice.
    Validate the user input.
    """
    print("Choose the type of mathematical operator you would like to play with.")
    print("You can choose from: add, subtract, multiply, divide")
    operators = ['add', 'subtract', 'multiply', 'divide']
    chosen_operator = ""
    chosen_operator = input("\nPlease enter your chosen mathematical operation: ").lower()
    
    while chosen_operator not in operators:
        print(f"'{chosen_operator}' is not a valid input.")
        chosen_operator = input(f"Please choose one of the operators {operators}: ").lower()

    return chosen_operator
    
def display_question(ops):
    """
    Generate a mathematical operation to be solved
    based on the user's selection of the operator.
    Repeat 5 times and return the score of correct answers.
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
                    given_result = int(input(f"\nQuestion: {num1} + {num2} = "))
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
            given_result = int(input(f"\nQuestion: {num1} - {num2} = "))
            if calculated_result == given_result:
                correct_score += 1
                print("That is correct!")
            else:
                print("Oh no, that is incorrect... ")
            i += 1

        if ops == 'multiply':
            calculated_result = num1 * num2
            given_result = int(input(f"\nQuestion: {num1} * {num2} = "))
            if calculated_result == given_result:
                correct_score += 1
                print("That is correct!")
            else:
                print("Oh no, that is incorrect... ")
            i += 1    

        if ops == 'divide':
            print("\nEnter your answer with one decimal place")
            #Ensure that numerator is larger than denominator
            if num1 < num2:
                num1 = num2
                num2 = num1
            calculated_result = round(num1 / num2, 1)
            given_result = round(float(input(f"\nQuestion: {num1} / {num2} = ")), 1)
            if calculated_result == given_result:
                correct_score += 1
                print("That is correct!")
            else:
                print("Oh no, that is incorrect... ")
            i += 1    

    print(correct_score)       
    return correct_score


if __name__ == "__main__":
    username = get_username()
    chosen_operator = choose_operation()
    correct_score = display_question(chosen_operator)
