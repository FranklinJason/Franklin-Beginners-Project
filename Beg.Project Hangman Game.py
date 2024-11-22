

import random

# List of all the words to guess later
words = ['coding', 'backup', 'update', 'download', 'python', 'database']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores
attempts = 8  # how many allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal the letter
    else:
        print("That letter doesn't appear in the word.")
        attempts -= 1

    # Check for repeated guesses or invalid input
    # Note: can actually make it better by making the version that can handle repeated guesses or validate input.
    

# Game ending or conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")
