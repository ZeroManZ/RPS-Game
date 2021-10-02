from random import randint 

print("Please , Fill Your Name Below ")
playername = input()
print('Hello ,',playername,'welcome to ROCK , PAPER & SCISSORS GAME. Have fun !')

print("Please choose : 0-rock | 1-paper | 2-scissors ")

player = input()
playerx = int(player)
if playerx >= 3 :
    print("Wrong Choice")
if playerx == 0 : 
    player = "rock"
if playerx == 1 : 
    player = "paper"
if playerx == 2 :
    player = "scissors"
print('your choice : ',player)

computer = randint(0,2)
if computer == 0 : 
    computer = "rock"
if computer == 1 : 
    computer = "paper"
if computer == 2 :
    computer = "scissors"

print('computer choice : ',computer)

if playerx == 2 :
    if computer == "scissors" :
        print("Result : Draw")
    if computer == "rock" :
        print("Result : Lose")
    if computer == "paper" : 
        print("Result : win")

if playerx == 0:
    if computer == "scissors" :
        print("Result : Win")
    if computer == "rock" :
        print("Result : Draw")
    if computer == "paper" : 
        print("Result : Lose")

if playerx == 1:
    if computer == "scissors" :
        print("Result : Lose")
    if computer == "rock" :
        print("Result : Win")
    if computer == "paper" : 
        print("Result : Draw")