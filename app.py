import random
import time

# List of words to choose from
words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]

# Hangman stages
def display_hangman(tries):
    stages = [
        """
           _____
          |     |
          |     |
          |     | 
          |     O
          |    /|\\
          |    / \\
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     | 
          |     O
          |    /|\\
          |    
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     | 
          |     O
          |    /|
          |    
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     | 
          |     O
          |     |
          |    
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     
          |     
          |     
          |    
        __|__
        """,
        """
           _____
          |     
          |     
          |     
          |     
          |     
          |    
        __|__
        """
    ]
    return stages[5 - tries]


# Main game function
def play_game():
    word = random.choice(words_to_guess)
    word_letters = set(word)
    guessed_letters = set()
    tries = 5
    display_word = ["_" for _ in word]

    print("\nWelcome to the Hangman Game!")
    name = input("Enter your name: ")
    print(f"Hello {name}, let's start the game!")
    time.sleep(1)

    while tries > 0 and set(display_word) != set(word):
        print(display_hangman(tries))
        print("Word:", " ".join(display_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
            print("Good guess!\n")
        else:
            tries -= 1
            print(f"Wrong guess! Tries left: {tries}\n")

    # Game result
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print(display_hangman(0))
        print("Sorry, you're hanged! The word was:", word)

    # Ask for replay
    replay = input("\nDo you want to play again? (y/n): ").lower()
    if replay == "y":
        play_game()
    else:
        print("Thanks for playing. Goodbye!")

# Start the game
if __name__ == "__main__":
    play_game()
