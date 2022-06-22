
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


import random
from word_list import word_list

chosen_word = random.choice(word_list)

lives = 6
display =[]
end_of_game = False
word_length = len(chosen_word)

for position in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Enter a letter: ")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You Lose, the word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print(f"You win. The word was {chosen_word}")

    print (''.join(display))
    print (stages[lives])
    