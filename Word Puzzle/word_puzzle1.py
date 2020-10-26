import random

def display_instructions():
    instructions = open("wp_instructions.txt", 'r')
    print(instructions.read())
    instructions.close

#def puzzle_progress():
    #list(word)

#display instructions by calling user defined function 
display_instructions()

#get wordlist
word_list = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']

#choose a random word from wordlist
word = random.choice(word_list)
#assign variable 'length' to length of word 
length = len(word)
#print 'length' number of '_'
answer_so_far = " _ "*length
print("The answer so far is", answer_so_far)

#make max number of guesses equal to 4
guess_number = 4

#while loop that executes as long as guesses are above 0
while guess_number > 0:
    for letter in word:
        #ask for a letter guess
        letter_guess = input("Guess a letter (" + str(guess_number) + " guesses remaining): ")
        if letter_guess in word:
            print(letter_guess)
            
        else: 
            print("The answer so far is", answer_so_far)
            guess_number = guess_number - 1

#replace element with letter          

#print number of guesses left
#deduct 1 guess if letter guessed is not within word