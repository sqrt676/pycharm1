def printBoard():
    print(f" 0 | 1 | 2 ")
    print("---------------")
    print(f" 3 | 4 | 5 ")
    print("---------------")
    print(f" 6 | 7 | 8 ")


if __name__=="__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0]
    turn=1
    print("Welcome to Tic Tac Toe")
    while(True):
        printBoard()
        if(turn==1):
            print("X's chance")
            value = int(input("Plz enter a val"))
            xstate[value] = 1
        else:
            print("X's chance")
            value = int(input("Plz enter a val"))
            xstate[value] = 1
