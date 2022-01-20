import random
import time
user = 0
comp = 0
draw = 0
while True:

    x = input("Please choose: p-paper, s-scissors, r-rock or 0-game end: ")
    if x == '0': break
    elif x == 'p' : x = "paper"
    elif x == 's' : x = "sciccors"
    elif x == 'r' : x = "rock"
    else:
        print("Please make the correct choice :")
        print("p - paper")
        print("s - sciccors")
        print("r - rock")
        print("0 - game end")
        continue

    y = random.choice(["paper", "sciccors", "rock"])

    print(" ")
    print("Your choice: ", x)
    print(" ")

    for i in range (0,3):
        print(3-i)
        time.sleep(1)
        
    print (" ")
    print ("Opponent: ", y)

    if x == y:
        draw += 1
    elif x == "paper" and y == "sciccors":
        comp += 1
    elif x == "paper" and y == "rock":
        user += 1
    elif x == "sciccors" and y == "rock":
        comp += 1
    elif x == "sciccors" and y == "paper":
        user += 1
    elif x == "rock" and y == "paper":
        comp += 1
    elif x == "rock" and y == "sciccors":
        user += 1
        
    print (" ")
    print ("Total results: ")
    print ("User: ", user)
    print ("Opponent: ", comp)
    print ("Dead-Heat: ", draw)

