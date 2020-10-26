# Remember The Word Description Outline
import os, time, random


if os.name == 'posix':
    clear_command = 'clear'
else:
    clear_command = 'cls'

header_content = 'Remember the Word'
header_border = '-' * 80
seconds_sleep = 1
# clear the screen
os.system(clear_command)
# display header 
print(header_border)
print(header_content)
print(header_border)

# display instructions
infile = open('instruction.txt', 'r')
content = infile.read()
print(content)

# prompt the player to press enter to continue
input("Press enter key to display the words.")
    
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

all_words = ['orange', 'chair', 'sandwich', 'mouse']
for word in all_words: 
    print(word)
    time.sleep(seconds_sleep)
    # clear the screen
    os.system(clear_command)
    # display header 
    print(header_border)
    print(header_content)
    print(header_border)


# prompt the player to enter the answer
#    - question is formulated using the first letter of the correct answer
#    - the correct answer is randomly chosen from one of the displayed words
letters = ['o', 'c', 's,' 'm']
question_letter = random.choice(letters)
answer = input('What word begins with the letter ' + question_letter + '?')

# display feedback
if question_letter == 'o':
    if answer == all_words[0]:
        print("You are correct. The answer was orange.")
elif question_letter == 'c':
    if answer == all_words[1]:
        print("You are correct. The answer was chair.")
elif question_letter == 's':
    if answer == all_words[2]:
        print("You are correct. The answer was sandwich.")
elif question_letter == 'm':
    if answer == all_words[3]:
        print("You are correct. The answer was mouse.")
else:
    print('Sorry, you entered ' + answer + '. The answer was ran.')
# prompt the player to play again
input("Play again? (y/N)") 
