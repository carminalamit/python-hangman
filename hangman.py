from random import choice
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''


# Hangman Figures
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["SHIHTZU", "FRENCHBULLDOG", "SHIBAINU", "POODLE","CHOWCHOW","DOBERMAN", "BEAGLE", "LABRADOR", "PUG", "POMERANIAN", "SYBERIANHUSKY"]

max_wrong = len(stages) - 1

# Initialize Variables

# Choose a word from word_list
word = choice(words)

# Dashes for each letter in a word
current_guess = "_ " * len(word) # times how many letters in a word

# When guess letter is wrong counter
wrong_guesses =  0

# Tracker of used letters
used_letters = []

# Intro
print("\033[1;31m" + logo +  "\033[0m")
print("Welcome to Hangman!")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("\nTry to Guess the Word")
print("\nHint: Dog breeds")

# Main Loop
while wrong_guesses < max_wrong and current_guess != word:
  print(stages[wrong_guesses])
  print("Used Letters: ", used_letters)
  print("So far, the word is: ", current_guess)

  guess = input("Type your letter guess here: ")
  guess = guess.upper() 
  # Nest loop
  # Check if letter was already used
  while guess in used_letters:
    print("You have already guessed that letter", guess)
    guess = input("Type your letter guess here: ")
    guess = guess.upper()
  # Add new guessed letter to the list of guesses letter
  used_letters.append(guess)

  # Check if guessed letter is in word
  if guess in word:
    print("Nice! You guessed it right!")
  
    # Give a new version of the word with dashes and mix of letters
    new_current_guess = ""
    for letter in range(len(word)):
      if guess == word[letter]:
        new_current_guess += guess
      else:
        new_current_guess += current_guess[letter]

    current_guess = new_current_guess
  else:
    print("Sorry your guessed letter is wrong")
    # Increase the number of incorrect by 1
    wrong_guesses += 1

# End of the game
if wrong_guesses == max_wrong:
  print(stages[wrong_guesses])
  print("You were hanged!")
  print("the correct word is: ", word)
else:
  print("Congo!! You won. :)")







