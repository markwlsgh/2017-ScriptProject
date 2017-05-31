from internet import *

loopFlag = 1
def printMenu():
    print("C8")
    print("======================Menu=====================")
    print("Test d")
    print("NN : a")
    print("B2 : q")
    print("===============================================")


def launcherFunction(menu):
    if menu == 'd':
        Date_Showing_Parsing()
    elif menu == 'a':
        Area_Showing_Parsing()
    elif menu == 'q':
        Quit()
        print("Good bye!")


def Quit():
    global loopFlag
    loopFlag = 0

while(loopFlag > 0):
    printMenu()
    menuKey = str(input("Hello : "))
    launcherFunction(menuKey)