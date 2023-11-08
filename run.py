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
    chosen_operator = input("Please enter your chosen mathematical operation: ").lower()
    
    while chosen_operator not in operators:
        print(f"'{chosen_operator}' is not a valid input.")
        chosen_operator = input(f"Please choose one of the operators {operators}: ").lower()

    return chosen_operator


if __name__ == "__main__":
    get_username()
    choose_operation()