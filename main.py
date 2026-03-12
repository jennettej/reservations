"""
SENG 201 - Term Project
Starter Script

Description:
    TODO: Describe what this program/module is supposed to do.
"""


FILE_NAME = "accounts.txt"

def create_account():

    print("\nWelcome to our hotel system\n\n\n")
    print("Please create an account\n")
    username = input("Please enter your username: ").strip()
    password = input("Please enter your password: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Account Created Successfully")

def main():
    """
    Main entry point for the program.
    """
    # TODO: Implement program logic here
    create_account()


if __name__ == "__main__":
    main()
