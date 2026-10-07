import random

words = ["python", "coding", "computer", "developer", "program"]
secret_word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_wrong_guesses} wrong guesses available.")


while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        print("The word was:", secret_word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")

else:
    print("\n Game Over!")
    print("The word was:", secret_word)