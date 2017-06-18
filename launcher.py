from internet import *

loopFlag = 1
def printMenu():
    print("======================Menu=====================")
    print("키워드 검색= 1")
    print("행사 검색= 2")
    print("주변 검색 = 3")
    print("숙박업소 검색 = 4")
    print("상세정보 검색 = 5")
    print("종료 = q")
    print("===============================================")


def launcherFunction(menu):
    if menu == '1':
        FindingKeyword()
    elif menu == '2':
        SearchFestival()
    elif menu == '3':
        SearchNear()
    elif menu == '4':
        SearchStay()
    elif menu == '5':
        detailCommon()
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