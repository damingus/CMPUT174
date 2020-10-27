#this program prompts the user to guess for a number between 1 and 10.
import random
random_number = random.randint(1,10) #We choose a random number between 1 and 10

print("I am thinking of a number between 1 and 10.")
guess = input("What number is it?")
print("The number was ",random_number)
print("Your guess was ",guess)