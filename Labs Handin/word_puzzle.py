# this program is a game where a user must correctly guess the letters in an unknown word before all of their guesses run out.
import random 

# this function chooses a random word from the given word list using random.choice
def word_bank():
    word_list = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango'] 
    word = random.choice(word_list) 
    return word

# this function opens, reads, and closes the given instruction.txt
def instruction():
    instructions = open("wp_instructions.txt", 'r') 
    print(instructions.read()) 
    instructions.close 

# this function creates 3 empty lists, and appends a given letter or underscore based on the letter (or number of letters) in the chosen word
def create_lists(word):
    word_as_list = [] 
    puzzle = [] 
    letter_list = [] # empty list to use for later in game
    
    # for each letter of randomly chosen word, we will append 1 underscore to puzzle_list and the letter to word_as_list
    for letter in word: 
        puzzle.append(" _ ") 
        word_as_list.append(letter) 
    return puzzle, word_as_list, letter_list 

# this function updates the lists, such that if  the letter guess is within the word_as_list, then the corresponding letter will be updated into the puzzle list.
def puzzle_update(word_as_list, letter_guess, puzzle, letter_list):
    # indexes each letter in word_as_list with with a value starting from 0 to length
    # for each, check if letter_guess is the same as a letter in word
    # if they are the same, then we update the puzzle index  with the letter index
    for index in range(len(word_as_list)): 
        if letter_guess == word_as_list[index]:
            puzzle[index] = word_as_list[index] 
            letter_list.append(letter_guess) # add a correct letter into the empty letter_list 
        
# this function checks to see when the game is over by checking if the length of the correctly guessed letters equal the number of letters from the original
def game_over(word_as_list, letter_guess, puzzle, guess_amount, letter_list, word):
    if len(letter_list) == len(word_as_list): 
        print("Good job! You found the word " + word + "!")  
        return 0 # exit loop if game is won by returning false

    # if the letter_guess is not in the word, then we will subtract a guess 
    elif letter_guess not in word: 
        guess_amount = guess_amount - 1
        # once the number of guesses left reaches 0, we print the answer.
        if guess_amount == 0: 
            print("The answer so far is", ''.join(puzzle)) 
            print("Not quite, the correct word was "+ word + ". Better luck next time")
    return guess_amount 

def main():
    instruction() 
    word = word_bank()
    puzzle, word_as_list, letter_list = create_lists(word) 
    guess_amount = 4
    while guess_amount > 0:
        print("The answer so far is", ''.join(puzzle)) #prints updated puzzle using .join function to replace the commas and brackets of a list with empty space
        letter_guess = input("Guess a letter (" + str(guess_amount) +" guesses remaining): ") #user input for letter_guess

        puzzle_update(word_as_list, letter_guess, puzzle, letter_list)
        guess_amount = game_over(word_as_list, letter_guess, puzzle, guess_amount, letter_list, word) #makes running dependent on function return
    input("Press enter to end the game.") #prompt user to end the game
main()
        