#=====importing libraries===========
'''This is the section where you will import libraries'''

# Import date library as this will be needed for automatically entereing the 
# current date that a task is entered. 
# Learned from https://ioflood.com/blog/python-get-current-date/

from datetime import date


#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''

# Ask the user to enter username and password and store in variables

username = input("Enter your username: ")
password = input("Enter your password: ")

# Create an empty dictionary that you'll be using to populate the usernames 
# and passwords in the 'user.txt' file.
# Split each line of user.txt into separate words and then add to the dictionary

u_and_p = {}

with open('C:/Users/Martin/Dropbox/MC23110010530/1 - Python for Data Science/L1T15 - Capstone Project - Files/10-020 Capstone Project - Files/user.txt', 'r') as file:
    for line in file:
        list = line.split(", ")
        u_and_p[list[0]] = list[1]

# While the username is not in the list, get the user to re-enter

while u_and_p.get(username) is None:
    username = input("Username not recognised, please enter again: ") 

# Because the password always seems to carry over a '/n' when entered onto 
# user.txt below, I needed to strip away the extra letter when comparing 
# it to the entered password. 
# I compare the entered password to that (trimmed_password) and the actual 
# password (because the most recently entered password in user.txt doesn't 
# yet have a '\n' attached to it.)
# Keep asking to reenter password until it's correct

trimmed_password = u_and_p[username][:-1]

while (trimmed_password != password) and (u_and_p[username] != password):
    password = input("Password not correct, please try again: ")



print()
print("You have succesfully logged in.")
print()
           


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
st - show statistics
e - exit
: ''').lower()

    if menu == 'r':
        #pass
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        # Add an if statement to only show the options to admin.

        if username == "admin":

            new_username = input("Please enter the username that you want to add: ")
            new_password = input("Please create a password: ")
            new_password_confirm = input("Please confirm password: ")

        # if both entered passwords are identical, write it to the user.txt file.
        # Use 'a' so it appends the text after the last existing text in the file.
        # Start with '\n' so that it starts on a new line. 

            if new_password == new_password_confirm:
                with open('C:/Users/Martin/Dropbox/MC23110010530/1 - Python for Data Science/L1T15 - Capstone Project - Files/10-020 Capstone Project - Files/user.txt', 'a') as file:
                    file.write("\n" + new_username + ", " + new_password)
            else:
                print("\nPasswords do not match. Select 'r' if you want to try again. \n")

        else:                 # If anyone other than admin attempt to add user
            print()
            print("You do not have the authority to add a user:")
            print()

    elif menu == 'a':
        #pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

        # I learned how to do current date from https://ioflood.com/blog/python-get-current-date/

        # Create variables for all the info needed and ask the user to enter them.

        from datetime import date
        task_person = input("Enter the username of the person assigned to the task: ")
        task_title = input("Enter the title of the task: ")
        task_desription = input("Write a brief description of the task: ")
        task_due = input("Enter the due date of the task: ")
        current_date = str(date.today())

        # Add a line with all the above info and also 'no' to indicate the 
        # task is incomplete. 

        with open('C:/Users/Martin/Dropbox/MC23110010530/1 - Python for Data Science/L1T15 - Capstone Project - Files/10-020 Capstone Project - Files/tasks.txt', 'a') as f:
            f.write("\n" + task_person + ", " + task_title + ", " + task_desription + ", " + current_date + ", " + task_due + ", " + "No")


    elif menu == 'va':
        #pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        # Take each line in tasks.txt and convert it into a list of separate 
        # strings. For every line in the file, print out the subheading in bold
        # and add the relevent string.

        with open('C:/Users/Martin/Dropbox/MC23110010530/1 - Python for Data Science/L1T15 - Capstone Project - Files/10-020 Capstone Project - Files/tasks.txt', 'r') as fi:
            for line in fi:
                breakdown = line.split(", ")
                
                # Make

                print()
                print("\033[1mTask: \033[0m            " + breakdown[1])
                print("\033[1mAssigned to: \033[0m     " + breakdown[0])
                print("\033[1mDate assigned: \033[0m   " + breakdown[3])
                print("\033[1mDue date: \033[0m        " + breakdown[4])
                print("\033[1mTask complete? \033[0m   " + breakdown[5])
                print("\033[1mTask description: \033[0m")
                print("  " + breakdown[2])
                print()
                print("____________________________________________________")
                print()

    # Use the same method as above, but first do an if statement to see
    # if the username is the same as the assigned name. If so, print
    # out the text as above.

    elif menu == 'vm':
        #pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        
        
        
        with open('C:/Users/Martin/Dropbox/MC23110010530/1 - Python for Data Science/L1T15 - Capstone Project - Files/10-020 Capstone Project - Files/tasks.txt', 'r') as fi:
            for line in fi:
                breakdown = line.split(", ")
                #print(breakdown)
                if username == breakdown[0]:
                    print()
                    print("\033[1mTask: \033[0m            " + breakdown[1])
                    print("\033[1mAssigned to: \033[0m     " + breakdown[0])
                    print("\033[1mDate assigned: \033[0m   " + breakdown[3])
                    print("\033[1mDue date: \033[0m        " + breakdown[4])
                    print("\033[1mTask complete? \033[0m   " + breakdown[5])
                    print("\033[1mTask description: \033[0m")
                    print("  " + breakdown[2])
                    print()
                    print("____________________________________________________")
                    print()

    # if username == admin, count the number of tasks by using a counter to 
    # add up each line in the task.txt file. 
    # Do the same with the user.txt file.
    # Print it out in a reader friendly way.

    elif menu == 'st':
        if username == "admin":
            with open('C:/Users/Martin/Dropbox/MC23110010530/1 - Python for Data Science/L1T15 - Capstone Project - Files/10-020 Capstone Project - Files/tasks.txt', 'r') as fi:
                task_counter = 0
                for line in fi:
                    task_counter +=1
            print()
            print("Number of current tasks: " + str(task_counter))
        
            with open('C:/Users/Martin/Dropbox/MC23110010530/1 - Python for Data Science/L1T15 - Capstone Project - Files/10-020 Capstone Project - Files/user.txt', 'r') as file:
                user_counter = 0
                for line in file:
                    user_counter +=1
            print("Number of users on system: " + str(user_counter))
            print()
        
        else: 
            print()
            print("Only admin has authority to see this information: ")
            print()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")