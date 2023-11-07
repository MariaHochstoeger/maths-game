print("Welcome to the Maths Game!")
print("Here you can test your knowledge in maths.")
print("You can choose which mathematical operation you would like to practice.")
print("You will play 5 rounds. Then you get your score.")
print("Let's start!\n")

def get_username():
    username = ""
    username = input("Please enter your name: ").strip()

    while username == "":
        username = input("You did not enter anything. Please enter a valid name: ")

    print(f"\nHello {username}!\n")
    return username

get_username()