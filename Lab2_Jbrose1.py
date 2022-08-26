"""
@author Jbrose1

Date: 2/9/22
"""
import numpy as np

again = True

while again:
    Player1 = np.random.randint(1,4)

    print('Pick one of these options Rock - 1, Scissors - 2, Paper - 3')
    Player2 = int(input("Player 2 pick something: "))

    result = 0

    choices = {1:'rock', 2:'Scissors', 3:'Paper'}

    if(Player1 == 1 and Player2 == 1):
        result = 0
    elif(Player1 == 2 and Player2 == 2):
        result = 0
    elif(Player1 == 3 and Player2 == 3):
        result = 0
    elif(Player1 == 1 and Player2 == 2):
        result = 1
    elif(Player1 == 1 and Player2 == 3):
        result = 2
    elif(Player1 == 2 and Player2 == 1):
        result = 2
    elif(Player1 == 2 and Player2 == 3):
        result = 1
    elif(Player1 == 3 and Player2 == 2):
        result = 2
    elif(Player1 == 3 and Player2 == 1):
        result = 1

    if(result == 1):
        print("Player1 Picked: {}".format(choices[Player1]))
        print("Player2 Picked: {}".format(choices[Player2]))
        print("*** Player 1 Wins! ***")
    elif(result == 2):
        print("Player1 Picked: {}".format(choices[Player1]))
        print("Player2 Picked: {}".format(choices[Player2]))
        print("*** Player 2 Wins! ***")
    else:
        print("Player1 Picked: {}".format(choices[Player1]))
        print("Player2 Picked: {}".format(choices[Player2]))
        print("*** Draw! ***")
    decision = input("do you want to continue? ")
    if decision == "no":
        again = False
print('See ya!')
