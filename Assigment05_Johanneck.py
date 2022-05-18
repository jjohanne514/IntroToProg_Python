# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files.
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table".
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jason Johanneck, 5/15/2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # The list to write to disk; Gets cleared after user chooses to Save Tasks to Disk
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
task = ""

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows 
# (like Lab 5-2)
objFile = open(strFile, "r")
print("\nContents of ToList.txt ... \n")
print("Task|Rank")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    print(lstRow)
    print(lstRow[0],"|",lstRow[1].strip())
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """ )
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print(lstTable)
        print("Task|Rank")
        for row in lstTable:
            print(row["task"],"|",row["rank"])
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task,rank = input('Enter Task,Rank: ').split(',')
        dicRow = {"task":task,"rank":rank}
        print("You entered ", dicRow)
        #append task & rank to hold table
        lstTable.append(dicRow)
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        task = input('Enter Task to remove: ')
        found = 'n'
        print(task)
        print(lstTable)
        for row in lstTable:
            if row["task"].lower() == task.lower():
                lstTable.remove(row)
                found = 'y'
        if found == 'y':
            print("task",task,"removed")
        else:
            print("task",task,"not found")
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "a")
        for row in lstTable:
            objFile.write(row["task"] + ',' + row["rank"] + '\n')
        objFile.close()
        #clear hold table
        lstTable = []
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("\nExiting Task List Program")
        break  # and Exit the program
