#Tic-tac-toe 
import sys
from os import system
arr=[[0,0,0],[0,0,0],[0,0,0]]
def stat():
    print( arr[0],"\n",arr[1],"\n",arr[2])
    #print(arr1)
    #print(arr2)
    #print(arr3)
#___________________________________________________________________________________________________________________________________
def check():
    #Horizontal check
    if (arr[0][1]+arr[0][1]+arr[0][2])==3 or (arr[1][0]+arr[1][1]+arr[1][2])==3 or (arr[2][0]+arr[2][1]+arr[2][2])==3:
        print("X wins!!!")
        sys.exit(0)
    elif (arr[0][1]+arr[0][1]+arr[0][2])==-3 or (arr[1][0]+arr[1][1]+arr[1][2])==-3 or (arr[2][0]+arr[2][1]+arr[2][2])==-3:
        print("O wins!!!")
        sys.exit(0)
    
    #Vertical check
    sum1=int(0)
    for i in range(0,3):
        for j in range(0, 3):
            sum1=sum1+int(arr[j][i])
        if sum1==int(3):
            print("X wins!!!")
            sys.exit(0)
        elif sum1==int(-3):
            print("O wins!!!")
            sys.exit(0)
        sum1=0

    #Horizontal check
    if((arr[0][0]+arr[1][1]+arr[2][2])==3 or (arr[0][2]+arr[1][1]+arr[2][0])==3):
        print("X wins!!!")
        sys.exit(0)
    elif((arr[0][0]+arr[1][1]+arr[2][2])==-3 or (arr[0][2]+arr[1][1]+arr[2][0])==-3):
        print("O wins!!!")
        sys.exit(0)
#__________________________________________________________________________________
def inputX(i,j):
    if arr[i][j]==0:
        arr[i][j]=1
        return True
    else:
        print("Invalid move for X")
        return False
def inputO(i,j):
    if arr[i][j]==0:
        arr[i][j]=-1
        return True
    else:
        print("Invalid move for O")
        return False
#__________________________________________________________________________________
def display():
    print("   1 2 3")
    for k in range(0,3):
        print((k+1)," ", end='')
        for l in range(0,3):
            if arr[k][l]==1:
                print('X ', end='')
            elif arr[k][l]==-1:
                print('O ', end='')
            else:
                print('_ ', end='')
        print()
#__________________________________________________________________________________
def enterX():
    i, j=input("Enter position for player X : ").split()
    boolX=inputX(int(i)-1,int(j)-1)
    if boolX==False:
        enterX()
    _=system("clear")
    display()

def enterO():
    i, j=input("Enter position for player O : ").split()
    boolO=inputO(int(i)-1,int(j)-1)
    if boolO==False:
        enterO()
    _=system("clear")
    display()

def runner():
    print("Welcome to Tic Tac Toe")               
    while(True):
        _=system("clear")
        display()
        enterX()
        '''i, j=input("Enter position for player X : ").split()
        inputX(int(i)-1,int(j)-1)
        _=system("clear")
        display()'''
        check()
        enterO()
        '''i, j=input("Enter position for player O : ").split()
        inputO(int(i)-1,int(j)-1)
        _=system("clear")
        display()'''
        check()
#__________________________________________________________________________________
#__________________________________________________________________________________
runner()
