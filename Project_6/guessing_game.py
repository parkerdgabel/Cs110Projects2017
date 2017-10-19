# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #6, 10/05/17
# This program plays a guessing game with the user.
from random import randint
UPPERBOUND = 100


def main():
    haiku()
    play()


def haiku():
    print("Learning is living.")
    print("We are empty like the sky.")
    print("Why then do you cry?")
    print()


def guessing_game():
    print("I'm thinking of a number from 1 to ", UPPERBOUND)
    num = randint(1, UPPERBOUND)
    userNum = 0
    counter = 0
    while userNum != num:
        counter += 1
        userNum = int(input("Your guess? "))
        if userNum == num:
            print("You got it right in ", counter, " guesses!")
        elif userNum < num:
            print("It's higher.")
        else:
            print("It's lower.")
    return counter


def play():
    done = False
    guess = 0
    games = 0
    best = 0
    guess = guessing_game()
    lastGuess = guess
    totalGuess = guess
    games += 1
    best = games
    again = input("Do you want to play again? ")
    if again[0].lower() == 'y':
        done = False
    else:
        done = True
    while not done:
        guess = guessing_game()
        games += 1
        if guess < lastGuess:
            best = games
        totalGuess += guess
        lastGuess = guess
        again = input("Do you want to play again? ")
        if again[0].lower() == 'y':
            done = False
        else:
            done = True
    print()
    statistics(totalGuess, games, best)


def statistics(guesses, games, best):
    print("Overall results:")
    print("Total games   = ", games)
    print("Total guesses = ", guesses)
    print("Guesses/game  = ", round((guesses / games), 1))
    print("Best game     = ", best)


main()
