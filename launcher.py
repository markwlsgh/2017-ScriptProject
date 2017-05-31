from internet import *

loopFlag = 1
def printMenu():
    print("======================Menu=====================")
    print("Search Keyword = 1")
    print("Search Festival = 2")
    print("Search Near = 3")
    print("Search Stay = 4")
    print("Quit = q")
    print("===============================================")


def launcherFunction(menu):
    if menu == '1':
        FindingKeyword()
    elif menu == '2':
        SearchFestival()
    elif menu == '3':
        SearchNear()
    elif menu == 'q':
        Quit()
        print("Good bye!")


def Quit():
    global loopFlag
    loopFlag = 0

while(loopFlag > 0):
    printMenu()
    menuKey = str(input("Select Menu : "))
    launcherFunction(menuKey)