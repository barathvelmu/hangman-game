import random
from words import word_database

# IMPORTANT
# This script is heavily documented. If visiting, please give it a read. Thank you :) 

# This function simply gets the words that are in words.py. 
def word_generator():
    word = random.choice(word_database)
    return word.upper() # this is done such for easier comparison logic with user input


# function used to work with user input and returning to uppercase
def user_input():
    inputted_value = input("Please guess a letter or word with '' around it: ")
    print("\n") # giving space 
    print("=====================================================")
    print("\n")
    return inputted_value.upper()


def run_game(word):
    existing_letters = [] # holds the letters user guesses
    existing_words = [] # holds the words user guesses
    unguessed_field =  len(word) * "_" # simulating unguessed letters
    guessed = False # initial value set to false 
    tries = 6 # amount of tries: counted with the head, body, both arms, both legs


    print("Hello! Welcome to the game of Hangman! Let's get started!")
    print(hangman_visual(tries)) # initial state of hangman 
    print(unguessed_field) # initial state of word with all underscores
    print("\n") # new line 

    # logic for game during run time 
    while not guessed and not tries <= 0: # validation step 
        guess = user_input() # converting to compare

        # logic for guessing a letter
        if len(guess) == 1 and guess.isalpha(): # validating only characters from alphabet
            # logic if letter is already in "existing_letters" list 
            if guess in existing_letters: 
                print("This letter has ALREADY BEEN GUESSED", guess)
            # logic if letter is not in the word 
            elif guess not in word: 
                print(guess, "is not in the word.")
                tries -= 1 
                existing_letters.append(guess) 
            # logic if guess is right (only remaining case)
            else: 
                print("Nice,", guess, "is in fact the word!")
                existing_letters.append(guess)
            # logic for creating the word completion
                word_as_list = list(unguessed_field) # converting the "_" string to a list 
                indices = [i for i, letter in enumerate(word) if letter == guess] # list comprehension
                for index in indices:
                    word_as_list[index] = guess # replace each underscore index with the guess
                unguessed_field = "".join(word_as_list) # converting back to string 
                if "_" not in unguessed_field: # validating if "_" is in the string. If not, word has been guessed.
                    guessed = True

        # logic for guessing a word            
        elif len(guess) == len(word) and guess.isalpha():
            # logic if word is already in "existing_letters" list 
            if guess in existing_words:
                print("You already guessed the word", guess)
            # logic if word is already in "existing_letters" list 
            elif guess != word:
                print(guess, "is not the word.")
                tries = tries - 1
                existing_words.append(guess)
            # logic if word has been guessed 
            else:
                guessed = True
                unguessed_field = word

        # logic if person did not guess properly         
        else:
            print("That is not a valid guess.")
        print(hangman_visual(tries)) # current stage of hangamn
        print(unguessed_field) # current stage of word
        print("\n") # new line
    
    # checking if guess was correct or the user ran out of tries
    if guessed == True:
        print("You got in! Congratulations!")
    else:
        print("Good try! The word was " + word + ". Give it another go!")



# hangman visualization state from bottom up 
def hangman_visual(tries):
    stages = [  # hangman final stage: head, body, both arms, and both legs (last part)
                """
                   Try #6
                   --------
                   |      |
                   |      O   uh oh...
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # head, body, both arms, and one leg
                """
                   1 more tries remaining!!! 
                   --------
                   |      |
                   |      O   AHHH! I NEED HELP!
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   2 more tries remaining!! 
                   --------
                   |      |
                   |      O   NOOO!
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, body, and one arm
                """
                   3 more tries remaining!
                   --------
                   |      |
                   |      O   PLEASE
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and body
                """
                   4 more tries remaining 
                   --------
                   |      |
                   |      O   No ah omg
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   5 more tries remaining 
                   --------
                   |      |
                   |      O    Help!
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state (start)
                """
                
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



# putting everything together 
def main():
    word = word_generator() # getting a word 
    run_game(word) # taking that word, and running the game

    # logic to play again 
    while input("Play Again? (Y/N): ").upper() == "Y":
        #setting a word and running the game once more
        word = word_generator()
        run_game(word)


if __name__ == "__main__": # ability to run script on command line 
    main()