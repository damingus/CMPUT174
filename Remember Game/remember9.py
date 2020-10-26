import time
import os
import random
# Identify Duplicate Adjacent Line Groups - replace them with iterative statement - while or a for
# Limit the literals in my program
# If there are more than one occurence of a literal in your program
#    - assign the literal to an identifier first
#    - use the identifier instead of literal in all the occurences of the literal
# Advantages of Limiting Literals
#  1. modifying a program is easy and less error prone
#  2. give context or meaning to the literals in my program
# randomly sample the words from a list and randomly choose an answer
# make the program run multiple times until the player enters any input other than 'Y' or 'y'
reply = 'y'

while (reply == 'y' or reply == 'Y'):
    if os.name == 'posix':
        clear_command = 'clear'
    else:
        clear_command = 'cls'
        
    header_border = '*' * 80
    header_content = 'Guess The Word'
    
    # clear the screen
    os.system(clear_command)    
    # display header 
    print(header_border)
    print(header_content)
    print(header_border)
    
    # display instructions
    infile = open('instructions.txt')
    content = infile.read()
    print(content)
    infile.close()
    # prompt the player to press enter to continue
    input('Press enter key to display the words.')
    
    # clear the screen
    os.system(clear_command)    
    # display header 
    print(header_border)
    print(header_content)
    print(header_border)
    
    # display words
    #     - 4 words are picked randomly from a fixed list
    #     - words are displayed one at a time
    #     - there is some pause before the word disappears and the next word appears
    infile = open('words.txt','r')
    content = infile.read()
    infile.close()
    all_words = content.splitlines() 
    sampled_words = random.sample(all_words,4)
    
    answer = random.choice(sampled_words) 
    answer_start_letter = answer[0]
    pause_time_secs = 1
    for word in sampled_words:
        print(word)
        time.sleep(pause_time_secs)
        # clear the screen
        os.system(clear_command)    
        # display header 
        print(header_border)
        print(header_content)
        print(header_border)
    
    
    # prompt the player to enter the answer
    #    - question is formulated using the first letter of the correct answer
    #    - the correct answer is randomly chosen from one of the displayed words
    guess=input('What word begins with the letter '+answer_start_letter+'?')
    # display feedback
    if guess == answer:
        print('Congratulation you are correct.')
    else:
        print('Sorry you entered '+guess+'.')
    print('The answer was '+answer+'.')
    # prompt the player to play again
    reply = input('Play again?(y/N)')