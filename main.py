"""
SENG 201 - Term Project
Starter Script

Description:
    TODO: Describe what this program/module is supposed to do.
"""


FILE_NAME = "accounts.txt"

def create_account():
    print("\n\nPlease create an account\n")
    newusername = input("Please enter your username: ").strip()
    newpassword = input("Please enter your password: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(newusername + "," + newpassword + "\n")

    print("Account Created Successfully")



def login():
    print("\n\nTo log in, please enter your username and password.\n")
    username = input("Please enter your username: ").strip()
    password = input("Please enter your password: ").strip()

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")

                # Check if both match
                if username == stored_username and password == stored_password:
                    print("Login successful!")
                    return

        # If no match found after checking all lines
        print("Invalid username or password.")

    except FileNotFoundError:
        print("No accounts found. Please create an account first.")


def main():
    """
    Main entry point for the program.
    """
    # TODO: Implement program logic here
    while True:
        print("\nWelcome to our hotel system\n")
        print("1. Create an account")
        print("2. Already have an account (Login)")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")



if __name__ == "__main__":
    main()
