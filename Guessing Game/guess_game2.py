import random, string

#choose a random letter from a to z
def random_letter():
    letter = str.lower(random.choice(string.ascii_letters)) #convert the letter to a lowercase string to avoid the problem of different demicimal values for uppercase and lowercase letters
    letter = str(letter)
    print(letter)
    return letter

#open instructions.txt and read it
def instructions_open():
    instructions = open('instructions.txt', 'r')
    print(instructions.read())
    instructions.close
    print("I am thinking of a letter between a and z.")

def create_lists():
    guess_list = [] #empty list to store guesses
    difference_list = [] #empty list to store differences between letters
    return guess_list, difference_list
#loop asks for a letter guess, possibly repeatedly if the guess does not fulfill the requirements
def letter_guess(guess_list):
    #guess_list = [] #empty list to store guesses
    #difference_list = [] #empty list to store differences between letters
    guess = str.lower(input("Take a guess: ")) #convert the guess to a lowercase string to avoid the problem of different demicimal values for uppercase and lowercase letters
    
    #loop that executes so long as guess is not a letter or longer than 1 and is not part of the alphabet
    while not guess.isalpha() or len(guess) != 1:
        print("Invalid input")
        guess = input("Take a guess: ")
    guess_list.append(guess) #we add each guess to the list
    return guess

#main loop
def game_loop(letter, guess_list):
    guess_number = 0 #set guess number to 0 so we can track the total later in stats()
    guess = letter_guess(guess_list) #we take guess from the previous function
    #print(guess_list)
    while guess != letter: 
        if guess > letter:
            print("Your guess is too high.")
            guess = letter_guess(guess_list)
            guess_number = guess_number + 1 #add one to guess_number for failed guess
        elif guess < letter:
            print("Your guess is too low.")
            guess = letter_guess(guess_list)
            guess_number = guess_number + 1
    print("Good job, you guessed the correct letter!")
    return guess_number

def level(guess_number):
    #finds skill level based on the amount of guesses it took to find the correct letter
    if guess_number < 5:
        print("Level: Expert")
    elif guess_number >= 5 and guess_number <= 10:
        print("Level: Intermediate")
    else:
        print("Level: Beginner")



def check_worst_guess(letter, guess_list, difference_list, guess_number):
    order_letter = ord(letter) #we find the order of the correct letter and assign it

    for char in guess_list: #for each character in the guess_list we find the difference to the correct letter
        order_guess = ord(char)
        if order_letter >= order_guess:
            difference = order_letter - order_guess #find difference for all letters
            difference_list.append(difference)
        else:
            difference = int(order_guess) - int(order_letter)
            difference_list.append(difference)
    
    max_difference = max(difference_list)

    if order_letter >= order_guess:
        worst_guess = chr(order_letter - max_difference) #chr() found from https://en.wikibooks.org/wiki/Python_Programming/Text
    else:
        worst_guess = chr(order_letter + max_difference)
    return worst_guess
    
    #worst_guess(letter, guess_list, difference_list) #call worst_guess
    #print("Worst Letter Guess: ", worst_guess)
def worst_guess_print(guess_number, worst_guess):
    if guess_number != 0:
        print("Worst Letter Guess: ", worst_guess)
    else:
        print("Worst letter Guess: not available")    

def stats(guess_number, letter, guess_list, difference_list):
    print("--MY STATS--")  
    print("Number of Guesses: ", guess_number + 1) 
    level(guess_number) #calls level(guess_number) to print skill level
    worst_guess = check_worst_guess(letter, guess_list, difference_list, guess_number)
    worst_guess_print(guess_number, worst_guess)
    
def main():
    letter = random_letter()
    instructions_open()
    guess_list, difference_list = create_lists()
    guess_number = game_loop(letter, guess_list)
    stats(guess_number, letter, guess_list, difference_list)
    
    
main()