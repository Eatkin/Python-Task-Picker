"""What is the plan
I want to give the user options
1) Pick me a task
    It will open up the file
    If empty, tell us we need to add a task first
    Otherwise it pulls up a dictionary or list or whatever and shuffles it
    Then tells us the first one
2) Add a new task
    Asks us task name and then appends it to the file
3) Remove an old task
    Lists tasks then asks us which number to remove or type 0 to exit
"""

#Imports
from os.path import exists
from time import sleep
import random

filename="tasks.txt"

#Define our methods here
def main_menu():
    print("Welcome to task picker. What would you like to do?")
    print("1) Choose a task for me")
    print("2) Add a new task")
    print("3) Remove an old task")
    print("4) List all tasks")
    print("5) Exit")
    choice=0
    while (choice<1 or choice>4):
        try:
            choice=int(input())
            break
        except ValueError:
            print("Fuck off")
            
    if (choice==1):
        pick_task()
    elif (choice==2):
        add_task(False)
    elif (choice==3):
        remove_task()
    elif (choice==4):
        list_tasks()
    elif (choice==5):
        quit()
    
def pick_task():
    file=open(filename, "r")
    lines=file.readlines()
    _list=[]
    for line in lines:
        _list.append(line)

    #Add a line break to the final element to make it consistent with others
    #Otherwise letters can get cut off
    _list[len(_list)-1]+="\n"

    #Now pick a random item by shuffling the list and showing the first item
    random.shuffle(_list)
    print("You should do this:")
    print(_list[0], end="")
    sleep(2)
    main_menu()
    

def add_task(isEmpty):
    print("Type in your task and I'll add it")

    #Get our input
    while True:
        try:
            task=input("")
            break
        except (len(task)==0):
            print("Try actually typing something this time")

    #Now add it to the file
    file=open(filename, "a")
    _task=task

    #If the file is NOT empty we add a preceding line break
    if (not isEmpty):
        _task="\n"+_task
    
    file.write(_task)
    file.close()
    print("I've added your task")
    sleep(2)
    main_menu()

def remove_task():
    print("Here we'll pick a task to remove")
    
    #List out all the items and also save it to a list
    #We also get the number of items in the list
    file=open(filename, "r")
    lines=file.readlines()
    file.close()
    _list=[]
    i=1
    for line in lines:
        _list.append(line)
        print(str(i)+") "+line,end="")
        i+=1

    #We need to add a line break to the final list element
    _list[len(_list)-1]+="\n"
    
    print("\n")
    print("Which would you like to remove?")
    _max=i-1

    #Now we pick what to remove
    choice=0
    while (choice<1 or choice>_max):
        try:
            choice=int(input())
            break
        except ValueError:
            print("Fuck off")

    #Print out what we've removed, remove from the list then go overwrite the file
    print(_list[choice-1][:-1]+" removed")
        
    del _list[choice-1]

    #Now remove the line break from the final list element
    file=open(filename, "w")
    listSize=len(_list)

    #Make sure list isn't empty
    if (not listSize==0):
        _list[listSize-1]=_list[listSize-1][:-1]

        #Now write the new file
        for task in _list:
            file.writelines([task])

    file.close()
    sleep(2)
    
    if (_max==1):
        print("You have no more tasks, please add something")
        add_task(True)
    else:
        main_menu()

    

def list_tasks():
    print("Here are all your tasks:")
    #Open file and print everything out
    file=open(filename, "r")
    lines=file.readlines()
    file.close()
    _list=[]
    i=1
    for line in lines:
        _list.append(line)
        print(str(i)+") "+line,end="")
        i+=1

    print("\n")

    sleep(2)
    main_menu()

#Check file exists, if not create it
fileExists=exists(filename)
if (not fileExists):
    file=open(filename, "w")
    file.close()

#Now check if the file is empty or not
file = open(filename, "r")
file.seek(0)        #Go to beginning of the file
isEmpty=not file.read(1)

if (isEmpty):
    print("You have no tasks, add one now!")
    file.close()
    add_task(True)
else:
    file.close()
    main_menu()

