import random

hangman_stages = [
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
          |
          |
          |
         ===
    """
]

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

logo =  """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
     
"""



print(logo)

chosen_word = random.choice(word_list)
 #For debugging. 

#Creating an empty string.
placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
    
print(placeholder)

game_over = False

correct_letters = []

lives = 6

while not game_over:

    
    guess = input("Guess a letter:").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in correct_letters:
        print("You've already guessed that letter.")
        continue
        
    correct_letters.append(guess)

    #Check if the selected letter is present in the random word.
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)  

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives reamining: {lives}")

    if lives == 0:
        game_over = True    
        print("*********You lose!*********")

    if "_" not in display:
        game_over = True
        print("*********You WIN!*********")

    print(hangman_stages[lives])

input("Press ENTER to exit!")
    