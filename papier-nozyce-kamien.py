import random
import time
user = 0
comp = 0
remis = 0
while True:

    x = input("Proszę wybrać: p-papier, n-nożyce, k-kamień lub 0-koniec: ")
    if x == '0': break
    elif x == 'p' : x = "papier"
    elif x == 'n' : x = "nożyce"
    elif x == 'k' : x = "kamień"
    else:
        print("Proszę o dokonanie prawidłowego wyboru:")
        print("p - papier")
        print("n - nożyce")
        print("k - kamień")
        print("0 - koniec gry")
        continue

    y = random.choice(["papier", "nożyce", "kamień"])

    print(" ")
    print("Twój wybór: ", x)
    print(" ")

    for i in range (0,3):
        print(3-i)
        time.sleep(1)
        
    print (" ")
    print ("Przeciwnik: ", y)

    if x == y:
        remis += 1
    elif x == "papier" and y == "nożyce":
        comp += 1
    elif x == "papier" and y == "kamień":
        user += 1
    elif x == "nożyce" and y == "kamień":
        comp += 1
    elif x == "nożyce" and y == "papier":
        user += 1
    elif x == "kamień" and y == "papier":
        comp += 1
    elif x == "kamień" and y == "nożyce":
        user += 1
        
    print (" ")
    print ("Wyniki łacznie:")
    print ("Użytkownik: ", user)
    print ("Komputer: ", comp)
    print ("Remis: ", remis)
    print (" ")
