# this program is a game where the user guesses for a letter within the alphabet based on a 'lower' or 'higher' feedback.
import random, string

# choose a random letter from a to z, and return it
def random_letter():
    letter = str.lower(random.choice(string.ascii_letters)) #convert the letter to a lowercase string to avoid the problem of different demicimal values for uppercase and lowercase letters
    letter = str(letter)
    return letter

# open instructions.txt and read it
def instructions_open():
    instructions = open('instructions.txt', 'r')
    print(instructions.read())
    instructions.close
    print("I am thinking of a letter between a and z.")

# we create empty lists to store later guesses and differences and return them. 
def create_lists():
    guess_list = [] 
    difference_list = [] 
    return guess_list, difference_list

# we form a list to store the number of guesses, which we will assign in main. 
def create_guess_numbers_list():
    guess_numbers_list = []
    return guess_numbers_list

# this function asks the user to input a guess, reasks if it is not satisfactory, stores it into the guess list and finally returns the guess
# he parameter guess_list is type list and allows us to append the guesses to guess_list
# the parameter guess_numbers_list is type list and will allow us to use it in the game loop 
def letter_guess(guess_list, guess_numbers_list):
    guess = str.lower(input("Take a guess: ")) # convert the guess to a lowercase string to avoid the problem of different demicimal values for uppercase and lowercase letters
    
    # loop that executes so long as guess is not a letter or longer than 1 and is not part of the alphabet
    while not guess.isalpha() or len(guess) != 1:
        print("Invalid input")
        guess = input("Take a guess: ")
    guess_list.append(guess) # add each guess to the list
    return guess

# this function serves as the main loop; it provides feedback as to whether the user inputted guess is too low or too high, so long as the guess is incorrect.
# the parameter letter is type string, and is the program's chosen letter
# the parameter guess_list is type list, which we need because letter_guess requires it
# the parameter guess_numbers_list is type list, and for each guess made, the number of guesses will be appended to the list
def game_loop(letter, guess_list, guess_numbers_list):
    guess_number = 0 #set guess number to 0 so we can track the total later in stats()
    guess = letter_guess(guess_list, guess_numbers_list)  # assign guess to what is returned from letter_guess()
    
    while guess != letter: 
        if guess > letter:
            print("Your guess is too high.")
            guess = letter_guess(guess_list, guess_numbers_list)
            guess_number = guess_number + 1 #add one to guess_number for failed guess
            
        elif guess < letter:
            print("Your guess is too low.")
            guess = letter_guess(guess_list, guess_numbers_list)
            guess_number = guess_number + 1
        
    print("Good job, you guessed the correct letter!")
    return guess_number

# this function determines the skill level of the user based on the guess_number found in previous functions
# the parameter guess_number is type integer, and is what this function will be based on given its value
def level(guess_number):
    # finds skill level based on the amount of guesses it took to find the correct letter
    if guess_number < 5:
        print("Level: Expert")
    elif guess_number >= 5 and guess_number <= 10:
        print("Level: Intermediate")
    else:
        print("Level: Beginner")

# this function derives the worst guess- that is, the guess furthest away from the original letter by using values from order()
# the parameter letter is type string, and is the original letter
# the parameter guess_list is type list, which stores all of the user guesses
# the parameter difference_list is type list and stores the differences between the guess and the letter
# the parameter guess_number is type integer and stores the value of the total number of guesses
def get_worst_guess(letter, guess_list, difference_list, guess_number):
    order_letter = ord(letter) 
    if len(guess_list) > 1:
        for char in guess_list: # for each character in the guess_list we find the difference to the correct letter
            if char != letter: # fix glitch where if the letter was the same as the character, the code would fail to function properly.
                order_guess = ord(char)
                if order_letter >= order_guess:
                    difference = order_letter - order_guess #find difference for all letters
                    difference_list.append(difference)
                else:
                    difference = order_guess - order_letter
                    difference_list.append(difference)
        max_difference = max(difference_list) 
        if order_letter >= order_guess:
            worst_guess = chr(order_letter - max_difference) #chr() found from https://en.wikibooks.org/wiki/Python_Programming/Text
        else:
            worst_guess = chr(order_letter + max_difference)
    elif len(guess_list) == 1: 
        for char in guess_list:
            order_letter = ord(char)
        worst_guess = 'unavailable'
    print("Worst Letter Guess: ", worst_guess)
    
# this function is presents the stats of each game
# guess_number is a parameter of type int and we use it to track the number of guesses made
# all other parameters have been defined multiple times
def stats(guess_number, letter, guess_list, difference_list, guess_numbers_list):
    guess_number = guess_number + 1  # added 1 because guess number started at 0. I.e, if user won with 1 guess, the total guesses would be 0.
    guess_numbers_list.append(guess_number)
    print("--MY STATS--")  
    print("Number of Guesses: ", guess_number) 
    level(guess_number) # calls level(guess_number) to print skill level
    get_worst_guess(letter, guess_list, difference_list, guess_number)
 
# this function controls whether or the game will continue to be played or not
# the parameter game is of type Boolean and if false will terminate the game
def play_again(game):
    replay = input("Would you like to play again? Y/N ")
    if replay == 'Y' or replay == 'y':
        return game
    else:
        game = False
        return game

# this function determines the overall (average) skill level of the user across all games played by summing and dividing the values from guess_numbers_list
# the parameter guess_numbers_list is of type list and stores the number of guesses made per game
def find_overall_level(guess_numbers_list):
    average_guess = sum(guess_numbers_list)/len(guess_numbers_list)
    if average_guess < 5:
        print("Overall Skill: Expert")
    elif average_guess >= 5 and average_guess <= 10:
        print("Overall SKill: Intermediate")
    else:
        print("Overall Skill: Beginner")

# this function presents the overall stats by finding the minimum and maximum values from guess_numbers_list
# the parameters in this function have been defined
def summary_stats(game, guess_numbers_list):
    if game == False:
        print("---SUMMARY STATS---")
        print("Lowest Number of Guesses:", min(guess_numbers_list))
        print("Highest Number of Guesses:", max(guess_numbers_list))
        print("Average Number of Guesses:", sum(guess_numbers_list)/len(guess_numbers_list))
        find_overall_level(guess_numbers_list)

# this function represents a single round in the game, which we call in main so long as game == true
# the parameter guess_numbers_list is type list, and stores the number of guesses for the stats() function call
def play_one_round(guess_numbers_list):
        letter = random_letter()
        instructions_open()
        guess_list, difference_list = create_lists()
        guess_number = game_loop(letter, guess_list, guess_numbers_list)
        stats(guess_number, letter, guess_list, difference_list, guess_numbers_list)
    

def main():
    game = True 
    guess_numbers_list =  create_guess_numbers_list()
    while game == True:
        play_one_round(guess_numbers_list)
        game = play_again(game)
        summary_stats(game, guess_numbers_list)
    
    
main()