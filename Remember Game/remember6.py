# Remember The Word Description Outline
import os, time, random


def display_header():
    # clear the screen and displays header
    os.system(clear_command)
    print(header_border)
    print(header_content)
    print(header_border)

replay = 'y' 
while (replay == 'y' or replay == 'Y'):
    if os.name == 'posix':
        clear_command = 'clear'
    else:
        clear_command = 'cls'

    header_content = 'Remember the Word'
    header_border = '-' * 80
    seconds_sleep = 1
    display_header()

    # display instructions
    infile = open('instruction.txt', 'r')
    content = infile.read()
    print(content)

    # prompt the player to press enter to continue
    input("Press enter key to display the words.")
        
    display_header()

    # display words
    #     - 4 words are picked randomly from a fixed list
    #     - words are displayed one at a time
    #     - there is some pause before the word disappears and the next word appears

    infile = open('wordlist.txt', 'r')
    content = infile.read()
    infile.close()
    all_words = content.splitlines() #create a list and remove the newline character
    sampled_words = random.sample(all_words, 4)
    answer = random.choice(sampled_words) #choose answer

    for word in sampled_words: 
        print(word)
        time.sleep(seconds_sleep)
        display_header()

    question_letter = answer[0]
    answer_input = input('What word begins with the letter ' + question_letter + '?')

    # display feedback
    if answer_input == answer:
        print("You are correct. THe answer was ", answer + ".")
    else:
        print("Sorry, you entered", answer_input + ". The answer was ", answer + ".")

    # prompt the player to enter the answer
    #    - question is formulated using the first letter of the correct answer
    #    - the correct answer is randomly chosen from one of the displayed words

    # prompt the player to play again
    replay = input("Play again? (y/N)") 




