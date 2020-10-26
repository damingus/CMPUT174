import random, string

def random_letter():
    letter = random.choice(random.choice(string.ascii_lowercase))
    return letter


def instructions_open():
    instructions = open('instructions.txt', 'r')
    print(instructions.read())
    instructions.close
    print("I am thinking of a letter between a and z.")

def letter_guess():
    guess = input("Take a guess: ")
    
    #loop that executes so long as guess is not a letter or longer than 1
    while not guess.isalpha() or len(guess) != 1:
        print("Invalid input")
        guess = input("Take a guess: ")
    return guess

def game_loop(letter):
    guess = letter_guess()
    while guess != letter:
        if guess > letter:
            print("Your guess is too high.")
            guess = letter_guess()

        elif guess < letter:
            print("Your guess is too low.")
            guess = letter_guess()

    print("Good job, you guessed the correct letter!")

    
def main():
    letter = random_letter()
    instructions_open()
    game_loop(letter)
    
main()