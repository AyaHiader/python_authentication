from auth import signin, signup, signout

def main():
    while True:
        print(
"""\n
Please select an option:
1. Sign In
2. Sign Up
3. Sign Out
4. Exit""")
        
        try:
            command = int(input("Enter your command: "))
        except ValueError as e:
            print("Invalid choice, please try again.")
            continue

        match command:
            case 1:
                # username = input("Enter username")
                signin()
            case 2:
                signup()
            case 3:
                signout()
            case 4:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice, please try again.")
                

if __name__ == "__main__":
    main()
