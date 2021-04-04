# Importing libraries and word module
import random
from p3_C_STR_HangmanSim_YILDIZ_data import words

# Hangman steps
man = ["""
   -----
   |   |
       |
       |
       |
       |
==============""", """
  -----
  |   |
  O   |
      |
      |
      |
==============""", """
  -----
  |   |
  O   |
  |   |
      |
      |
==============""", """
  -----
  |   |
  O   |
 /|   |
      |
      |
==============""", """
  -----
  |   |
  O   |
 /|\  |
      |
      |
==============""", """
  -----
  |   |
  O   |
 /|\  |
 |    |
      |
==============""", """
  -----
  |   |
  O   |
 /|\  |
 | |  |
      |
=============="""]

# Choosing the word
def WordChoice(words):
    choice = random.choice(words)
    return choice

choice = WordChoice(words)

# Checking if the letter is true or not
def check(choice,letter):
    word = []
    increment = 0    
    for n in choice:
        if n == letter:
            word.append(increment)
        increment += 1
    if len(word) == 0:
        print("Your guess is not true!")
        return False
    else:
        print("Congratulations! The man is still alive (for now :) ).")
        return word
        
    

for k in range(0, len(choice)):
    print("_ ",end="")
print("")

# Playing the game
predicted_letters = []
wrong_letters = 0
game = len(man)

while game > 0:
    guess = input("Enter a letter: ")
    control = check(choice, guess)
    if control == False:
        print(man[wrong_letters])
        wrong_letters += 1
        game -= 1
    else:
        if wrong_letters == 0:
            print(man[wrong_letters])
        else:
            print(man[wrong_letters - 1])
        for i in control:
            predicted_letters.append(i)
        for i in range(0, len(choice)):
            if i in predicted_letters:
                print(choice[i], end="")
            else:
                print("_ ", end="")
        print("")
    if len(predicted_letters) == len(choice):
        game = -1

# The result
if game == 0:
    print("Sorry, the man has died! The reason for that you could not find the word %s." %choice)    
else:
    print("Thank God, you find the word!")
    