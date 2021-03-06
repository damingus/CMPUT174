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

def create_guess_numbers_list():
    guess_numbers_list = []
    return guess_numbers_list

def letter_guess(guess_list, guess_numbers_list):
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
def game_loop(letter, guess_list, guess_numbers_list):
    guess_number = 0 #set guess number to 0 so we can track the total later in stats()
    guess = letter_guess(guess_list, guess_numbers_list) #we take guess from the previous function
    #print(guess_list)
    while guess != letter: 
        if guess > letter:
            print("Your guess is too high.")
            guess = letter_guess(guess_list, guess_numbers_list)
            guess_number = guess_number + 1 #add one to guess_number for failed guess
        elif guess < letter:
            print("Your guess is too low.")
            guess = letter_guess(guess_list, guess_numbers_list)
            guess_number = guess_number + 1
        guess_numbers_list.append(guess_number)
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
        if char != letter: #fix glitch where if the letter was the same as the character, the code would fail to function properly.
            order_guess = ord(char)
            if order_letter >= order_guess:
                difference = order_letter - order_guess #find difference for all letters
                difference_list.append(difference)
            else:
                difference = order_guess - order_letter
                difference_list.append(difference)
    
    max_difference = max(difference_list)
    print(order_guess)
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

def play_again(game):
    replay = input("Would you like to play again? Y/N ")
    if replay == 'Y' or replay == 'y':
        return game
    else:
        game = False
        return game

def find_overall_level(guess_numbers_list):
    average_guess = sum(guess_numbers_list)/len(guess_numbers_list)
    if average_guess < 5:
        print("Overall Skill: Expert")
    elif average_guess >= 5 and average_guess <= 10:
        print("Overall SKill: Intermediate")
    else:
        print("Overall Skill: Beginner")

def summary_stats(game, guess_numbers_list):
    if game == False:
        print("---SUMMARY STATS---")
        print(guess_numbers_list)
        print("Lowest Number of Guesses:", min(guess_numbers_list))
        print("Highest Number of Guesses:", max(guess_numbers_list))
        print("Average Number of Guesses:", sum(guess_numbers_list)/len(guess_numbers_list))
        find_overall_level(guess_numbers_list)



def play_one_round(guess_numbers_list):
        letter = random_letter()
        instructions_open()
        guess_list, difference_list = create_lists()
        guess_number = game_loop(letter, guess_list, guess_numbers_list)
        stats(guess_number, letter, guess_list, difference_list)
    

def main():
    game = True
    while game == True:
        guess_numbers_list =  create_guess_numbers_list()
        play_one_round(guess_numbers_list)
        game = play_again(game)
        summary_stats(game, guess_numbers_list)
    
    
main()