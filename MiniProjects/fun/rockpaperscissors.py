import time
import random

userName = input("Enter your name: ")
options = ['rock', 'paper', 'scissors']
computer = random.choice(options)
userChoice = input('pick either rock, paper or scissors:')

print("rock")
time.sleep(1)
print("paper")
time.sleep(1)
print("scissors")
time.sleep(1)
print("shoot")
time.sleep(1)
print("Computer chose: " + computer)
print(userName + ": " + userChoice)
if computer == userChoice:
    print("Draw")
elif userChoice == 'rock' and computer == 'paper':
    print("Computer Wins")
elif userChoice == 'rock' and computer == 'scissors':
    print(userName + " Wins")
elif userChoice == 'paper' and computer == 'rock':
    print(userName + " Wins")
elif userChoice == 'paper' and computer == 'scissors':
    print("Computer Wins")
elif userChoice == 'scissors' and computer == 'rock':
    print("Computer Wins")
elif userChoice == 'scissors' and computer == 'paper':
    print(userName + " Wins")
else:
    print("You didnt enter rock, paper or scissors")
#possible options
#Player / Computer
#rock / paper
#rock / scissors
#paper / rock
#paper / scissors
#scissors / rock
#scissors / paper