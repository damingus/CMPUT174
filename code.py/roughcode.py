# this program decrypts a text using a few user defined functions

# Returns a string that has all the characters that are in word, in the same order, except for the ones that are in char_list\
# word is an object of type str
# char_list is an object of type list
def remove_chars(word, char_list):
    ecode = word
    word_list = list(word)
    decoded_word = ''
    for index in range(len(word)):
        if word_list[index] not in char_list:
            decoded_word = decoded_word + word_list[index]
    word = decoded_word
    return word, ecode

# Returns a string that has all the characters that are in word, in reverse order.
# word is an object of type str.
def rev_string(word):
    word_list = list(word)
    reversed_word = ''
    word_length = len(word)
    subtraction = word_length - 1 #we subtract one because the length of the word will be one more than the number of elements
# find length of word to find the total arrays
    for index in range(word_length):
        reversed_word = reversed_word + word_list[index + subtraction] 
        subtraction = subtraction - 2 #we need to subtract 1 more than necessary otherwise we will print the same letter for each index
    
    word = reversed_word
    return word

# Returns a string that has all the characters that are in word, in the same order except that 2 is subtracted from every alternate digit, starting with the first digit, that may occur inside the word. 
def sub_alt_num(word):
    #word_list = list(word)
    word_list = list(word)
    decoded_list = []
    alternate = 2
    # Make a new list with the elements in word_list as integers and strings based on their order number
    for index in range(len(word_list)):
        if ord(word_list[index]) >= 48 and ord(word_list[index]) <= 57:
            obtain_int = int(word_list[index])
            decoded_list.append(obtain_int)
        else:
            decoded_list.append(word_list[index])
    
    # for every integer in decoded_list, we will subtract 2 from. 
    # Use the remainder method to do so
    # update word_list with new integers
    for index in range(len(decoded_list)):
        if ord(str(decoded_list[index])) >= 48 and ord(str(decoded_list[index])) <= 57:
            if alternate%2 == 0:
                decoded_list[index] = decoded_list[index] - 2
            alternate = alternate + 1
        word_list[index] = decoded_list[index]
    
    #re-string integers in word_list so we can use the .join method
    for index in range(len(word_list)):
        word_list[index] = str(word_list[index])

    restring_word = ''.join(word_list)
    word = restring_word
    return word

# Returns a string that has all the characters that are in word, in the same order except that all 
# lowercase characters are changed to uppercase and vice versa (any numbers that may occur in the character sequence should not be changed).
def swap_cases(word):
    swapped_string = ''
    word_list = list(word)
    for index in range(len(word_list)):
        letter_order = ord(word_list[index])
        if letter_order >= 97 and letter_order <= 122:
            swapped_string = swapped_string + word_list[index].upper()
        elif letter_order >= 65 and letter_order <= 90:
            swapped_string = swapped_string + word_list[index].lower()
        else:
            swapped_string = swapped_string + word_list[index]
    
    dcode = swapped_string
    return dcode

# Displays the encrypted and decrypted code
# both parameters are type string
def display(ecode, dcode):
    print("Encrypted code:", ecode)
    print("Decrypted code:", dcode)

def main():
    code_txt = open("encrypted.txt", 'r') # open, read and close the encrypted file
    word = code_txt.read()
    code_txt.close
    char_list = ['#', '&', '!', '/'] # set the list of removed characters

    # update the word per each function
    word, ecode = remove_chars(word, char_list)
    word = rev_string(word)
    word = sub_alt_num(word)
    dcode = swap_cases(word)
    display(ecode, dcode)

main()





    
    


