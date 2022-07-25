import time
import random
import sys

print("""*************************
Number Guess Game (1-100)
*************************""")
while True:
    hearth = 10
    number = random.randint(1,100)
    while(hearth >= 0):
        if(hearth == 0):
            while True:
                print("R - You Lose, Try Again\nE - Exit ")
                c = input()
                if(c == 'R'):
                    break
                elif(c == "E"):
                    print("Goodbye")
                    sys.exit()
                else:
                    print("Please enter a valid input")
        try:
            guess = int(input("Guess: "))
            if(guess == number):
                while True:
                    print("R - You Won, Play Again\nE - Exit ")
                    c = input()
                    if(c == 'R'):
                        break
                    elif(c == "E"):
                        print("Goodbye")
                        sys.exit()
                    else:
                        print("Please enter a valid input")
            elif(guess < number):
                print("Your guess is smaller than number.")
                hearth -= 1
            else:
                print("Your guess is bigger than number.")
                hearth -= 1
        except ValueError:
            print("Please enter a valid number.")
            hearth -=1