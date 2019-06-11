# guessing game
import random

print("hello, please enter your name")
name = input()
print("hi", name)
print("here are the lists")
avengers = ["iron man", "thor", "captain america", "hawkeye"]
justiceleague = ["shazam", "superman", "batman", "aquaman"]
print(avengers)
print(justiceleague)
gameplay=True
while gameplay:
         print("what do you want to do?")
         print("1-play,,,,,,2-exit")
         option = int(input())
         while option==1:
                        print("please,choose one")
                        choice = input()
                        if choice == "avengers":
                                 print("here is the list", avengers)
                                 guess = random.choice(avengers)
                                 print("enter")
                                 user_guess = input()
                                 if guess == user_guess:
                                                   print("you are right i was thinking about", guess)
                                 else:
                                                   print("sorry,i was thinking about", guess)

                        if choice == "justiceleague":
                                 print("here is the list", justiceleague)
                                 guess = random.choice(justiceleague)
                                 print("enter")
                                 user_guess = input()
                                 if guess == user_guess:
                                                   print("you are right i was thinking about", guess)
                                 else:
                                                   print("sorry,i was thinking about", guess)
