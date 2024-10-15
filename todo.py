#!/usr/bin/env python3
#To-do list! By Jacob Mattie, Oct 14, 2024

import os

#Folder name:
fileName = "ToDo_List"

#Data file name (.txt)
toDo = "ToDoList_Contents"

linebreak = "--------------------------------------------------------------"


if not os.path.exists(fileName):
    os.makedirs(fileName)

programDirectory = os.path.dirname(os.path.realpath(__file__))  
dataDir = os.path.join(programDirectory, fileName)

os.chdir(dataDir)

def makeFile(fileName):
    with open(f"{fileName}.txt", "a") as file:
        file.write("")

def userInputInteger(inputList): #Prompts the user for an integer input within an allowable range (len(inputList)). UI. Returns index of selected list item, starting at 0
    numRange = len(inputList)
    editChoice = input("Enter the numeric value corresponding to your selection: ")
    while(True):
        if(editChoice.isdigit() == True):
            editChoice = int(editChoice)
            if (editChoice > 0 & editChoice <= numRange):
                return (editChoice - 1)
            else:
                editChoice = input("Your entered value is out of range! Please try again. \n")
                continue
        elif (editChoice == ""):
            return ""
        else:
            editChoice = input("Your entered value is not an integer! Please try again. \n")
            continue

def listString(list, buffer):   #UI. Lists options in a list with an associated index. Pairs with userInputInteger(list)
    num = 1
    for element in list:
        print(f"{buffer}{num} - {element}")
        num += 1
    print("\n")
    return

def printChoose(inputList):
    listString(inputList, "")
    choice = userInputInteger(inputList)
    return choice

def readFileList(fileName):
    with open(f'{fileName}.txt', 'r') as file:
        allLines = []
        for line in file: 
            allLines.append(line.strip())
        return allLines
    
def fileAppend(fileName, *lst):
    with open(f'{fileName}.txt', 'a') as file:
        for element in lst:
            file.write(f"{element}\n")

def removeLineN(fileName, n):
    fileName = fileName + ".txt"
    with open(fileName, 'r') as file:
        lines = file.readlines()
    del lines[n]
    with open(fileName, 'w') as file:
        file.writelines(lines)

if not os.path.exists(toDo + ".txt"):
        print(f"Created new file: {toDo}")
        makeFile(toDo)



choiceList = ["Add new task", "Mark a task as finished"]

while(True):
    print("Welcome! Let's get these tasks cranked out.\n\n")
    toDoList = readFileList(toDo)
    print("Current list: \n\n")
    if toDoList == []:
        print("\t\t ------ You're all caught up! Well done :) ------\n\n")
    else:
        listString(toDoList, "\t\t")
    print(linebreak + "\n")

    print("Select what you'd like to do:\n")
    choice = printChoose(choiceList)

    if choice == "":
        break
    elif choice == 0:
        newTask = input("Enter new task: \n")
        fileAppend(toDo, newTask)
    elif choice == 1: 
        print("Which task would you like to remove?\n")
        removeChoice = userInputInteger(toDoList)
        removeLineN(toDo, removeChoice)
    
