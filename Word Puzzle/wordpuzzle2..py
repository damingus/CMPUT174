import random

instructions = open("wp_instructions.txt", 'r')
print(instructions.read())
instructions.close

word_list = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango'] #provided word list to use
word = random.choice(word_list) #choose random word from word_list

letter_list = [] #empty list to use for later in game

word_as_list = [] #initial empty letter list
puzzle = [] #initial puzzle word list (_)


for letter in word: #for each letter of randomly chosen word, we will append 1 underscore to puzzle_list and the letter to word_as_list
    puzzle.append(" _ ")
    word_as_list.append(letter)


guess_amount = 4 #sets max amount of guesses to 4


while guess_amount > 0:

    print("The answer so far is", ''.join(puzzle)) #prints updated puzzle using .join function to replace the commas and brackets of a list with empty space
    letter_guess = input("Guess a letter (" + str(guess_amount) +" guesses remaining): ") #user input for letter_guess
    for index in range(len(word_as_list)): #indexes each letter in word_as_list with with a value starting from 0 to length
        if letter_guess == word_as_list[index]: #checks if letter_guess is the same as a letter in word, 1 by 1 until completion of word_as_list
            puzzle[index] = word_as_list[index] #updates the puzzle index with the letter index correspondingly if letter_guess is an element of word_as_list 
            letter_list.append(letter_guess) #add a correct letter into the empty letter_list 
            
    
    if len(letter_list) == len(word_as_list): #once the length of the letter_list equals the length of word_list we end the loop
        print("Good job! You found the word " + word + "!")  #Print winning message
        break #exit loop if game is won


    elif letter_guess not in word: #if the letter_guess is not in the word, then we will subtract a guess 
        guess_amount = guess_amount - 1
        if guess_amount == 0: #once the number of guesses left reaches 0, we print the answer.
            print("The answer so far is", ''.join(puzzle)) #Reuse function for printing answer since the loop ends at 0
            print("Not quite, the correct word was "+ word + ". Better luck next time")  
            


input("Press enter to end the game.") #prompt user to end the game






       
    


