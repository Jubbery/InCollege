# 5 unique student accounts
#Gianni, Anthony, Sebastian, Jack, and Rishabh's scrum baby
import sqlite3
import os
import lib.checkStrUtils as checkStrUtils
from lib.User import User
from lib.Job import Job

def postJobScreen(loggedInUser):
  clearConsole()
  con = sqlite3.connect("incollege.db")
  cur = con.cursor()
  res = cur.execute("SELECT COUNT() FROM jobs")
  userCount = res.fetchone()[0]
  print("Number of jobs: " + str(userCount))
  if (userCount >= 5):
      print(
          "\tReached limit on jobs posted.\n \tPlease come back later.\n"
      )
      return None
  title = input("Enter the Title of the position you are posting: ")
  
  description = input("Enter the description of the position: ")
  
  employer = input("Enter name of employer: ")
  
  location = input("Enter location of employer: ")
  salary = input("Enter salary for the position: ")

  job = Job()
  job.create(title, description, employer, location, salary, loggedInUser.getUserId())
  jobScreen(loggedInUser)
  
def jobScreen(loggedInUser):
  clearConsole()
  print("\n\tFind or post A Job\n")
  print("press \"1\" to search for a Job or internship.")
  print("press \"2\" to post a job")
  print("press \"3\" to return to the options screen")
  selection =int(input())
  if selection ==1:
    underConstructionScreen()
  elif selection ==2:
    postJobScreen(loggedInUser)
  elif selection ==3:
    optionsScreen(loggedInUser)

    
def findSomeoneScreen(loggedInUser):
    clearConsole()
    print("\n\tFind Someone you Know\n")
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    firstname = input(
        "Enter the first name of the person you are searching for: \n")
    firstname = firstname.lower()
    lastname = input(
        "Enter the last name of the person you are searching for: \n")
    lastname = lastname.lower()
    res = cur.execute(
        "SELECT user_firstname, user_lastname FROM users WHERE user_firstname = ? AND user_lastname = ? LIMIT 1",
        (firstname,lastname ))
    user = res.fetchone()
    if (user == None):
        print("They are not yet part of the InCollege system yet.")
    else:
        print("\nThey are a part of the InCollege System.")
        if(not loggedInUser):
	        print("\tWant to become a part of InCollege?")
	        print("\tLog-in or Sign-up to join your friends!\n")
	        print("Press \"0\" to return to home screen.")
	        print("Press \"1\" to log in using an existing account.")
	        loginI = int(input("Press \"2\" to create a new account.\n"))
	        if loginI == 1:
	        	login()
	        elif loginI == 2:
	        	signup()
	        elif loginI == 0:
	        	clearConsole()
	        	main()
	        else:
	        	print("invalid input")


def underConstructionScreen():
    print("\n\t~ Under Construction ~")


def clearConsole():
    os.system('clear')


def skillsScreen(loggedInUser):
    clearConsole()
    print("\n\tSkills Screen")
    print("Select a skill to learn: ")
    print(
        "\t1. Python\n\t2. SQL Databases\n\t3. PyTest\n\t4. Command Line Interface\n\t5. Machine Learning\n\t6. Return to Options\n"
    )
    selection = int(input(""))
    clearConsole()
    if selection==6:
      optionsScreen(loggedInUser)
    underConstructionScreen()


def optionsScreen(loggedInUser):
    print("\n\tOptions Screen")
    print("Select an option:")
    print("\t1: Search for a Job")
    print("\t2: Find someone you know")
    print("\t3: Learn a new skill")
    selection = int(input("\t4: Log out\n"))
    clearConsole()
    if selection == 1:
        jobScreen(loggedInUser)
    elif selection == 2:
        findSomeoneScreen(loggedInUser)
    elif selection == 3:
        skillsScreen(loggedInUser)
    elif selection == 4:
        main()


def checkIfUsernameIsUniqueInDB(username):
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute(
        "SELECT user_username FROM users WHERE user_username = ? LIMIT 1",
        (username, ))
    user = res.fetchone()
    return user == None


# 8-12 characters
# at least 1 cap letter
# at least 1 digit
# at least 1 special character
def checkPassword(password):
    if not checkStrUtils.checkIfStrIsCorrectLength(password, 8, 12):
        print("\tPassword must be 8-12 characters in length ")
        return False

    if not checkStrUtils.checkIfStrContainsUpperChar(password):
        print("\tPassword must contain at least 1 uppercase character ")
        return False

    if not checkStrUtils.checkIfStrContainsDigit(password):
        print("\tPassword must contain at least 1 digit ")
        return False

    if not checkStrUtils.checkIfStrContainsSpecialChar(password):
        print("\tPassword must contain at least 1 special character ")
        return False

    return True


def login():
    clearConsole()
    print("\n\tLogin Screen")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = User(None)
    user = tempUser.findOneByUsername(username)
    if (user == None or user[2] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()
    else:
        print("\tYou have successfully logged in\n")
       	clearConsole()
        loggedInUser = User(user[0])
        optionsScreen(loggedInUser)


def checkUsername(username):
    if (not checkStrUtils.checkIfStrIsCorrectLength(username, 1, 32)):
        print(
            "\tUsername must be between 1 and 32 characters!\n\tPlease try again.\n"
        )
        return False
    if (not checkIfUsernameIsUniqueInDB(username)):
        print("\tUsername must be unique!\n\tPlease try again.\n")
        return False
    return True


def signup():
    clearConsole()
    print("\tSignup Screen")
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute("SELECT COUNT() FROM users")
    userCount = res.fetchone()[0]
    print("Number of Users: " + str(userCount))
    if (userCount >= 5):
        print(
            "\tAll permitted accounts have been created.\n \tPlease come back later.\n"
        )
        return None
    username = input("Enter Username: ")
    while (not checkUsername(username)):
        username = input("Enter Username: ")
    password = input("Enter Password:")
    while (not checkPassword(password)):
        password = input("Enter Password: ")
    firstname = input("Enter First Name:")
    while (firstname == None):
        firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name:")
    while (lastname == None):
        lastname = input("Enter Last Name: ")
  
    newUser = User(None)
    newUser.create(username, password, firstname, lastname)
    print("\tAccount Created!\n")
    main()


def videoScreen():
    print("\n\tVideo is now playing\n")
    print("Press 1 to return to home screen.")
    print("Press 2 to replay video.")

    choice = int(input())

    if choice == 1:
        clearConsole()
        main()
    else:
        videoScreen()


def main():
    print("\tHome Screen")
    print(
        "\n\tJames was a student at the University of South Florida.\n\t He used InCollege to connect with employers and explore job opportunities.\n\t Through InCollege's internship programs, James earned an internship with Google which eventually turned into a full time employment opportunity for James.\n\t He now works as a senior software developer for Google.\n\t Watch our Video to learn more about how InCollege can help you find an internship or career opportunity!\n")
	
    print("Press \"1\" to learn more about how InCollege can help you find a career.")
    print("Press \"2\" to connect with an InCollege user.")
    print("Press \"3\" to log in using an existing account.")
    loginI = int(input("Press \"4\" to create a new account.\n"))
    clearConsole()
    if loginI == 1:
        videoScreen()
    elif loginI == 2:
        findSomeoneScreen(0)
    elif loginI == 3:
        login()
    elif loginI == 4:
        signup()
    else:
        print("invalid input")


if __name__ == "__main__":
    main()
