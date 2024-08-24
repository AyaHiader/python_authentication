# Define the file name (can be .csv or .txt)
import csv
FILE_NAME = 'users.csv'

# Function to sign up a new user
def signup():
    #Gather user input
    username = input("Enter username: ")
    first_name=input('Enter your first name:')
    last_name=input('Enter your last name:')
    password=input( "Enter your password:")
    age=int(input( "Enter your age:"))

#vaildate inputes
    with open(FILE_NAME, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
                if row[0] == username  :
                    print("Error: Username already exists  . Please try again.")
                    return
                elif age<0:
                    print("wrong try again")
                    return


    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, "False"])
        print("Signup successful!")

# Function to sign in an existing user
def signin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    updated_rows=[]
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            user_checker=[row[0],row[1]]
            if user_checker[0]==username :
                if user_checker[1]==password:
                    row[5]=True
                print("Signin successful!")
                break
        else:
            with open(FILE_NAME, mode='a', newline='') as file:
                writefile = csv.writer(file)
                writefile.writerow([username, password])
                writefile.writerows(updated_rows)
                print("Error: Incorrect username or password. Please try again.")



# Function to sign out an existing user
def signout():
    username = input("Enter username: ")
    updated_rows = []
    success = False
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[0] == username :
                success = True
            updated_rows.append(row)
    
    if success:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            writer.writerows(updated_rows)
        print("Signout successful!")
    else:
        print("Error: User is not logged in or does not exist.")