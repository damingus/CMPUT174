#This program sees whether 2 inputted temperatures are equal or not
#assign 'a' to the first temperature we ask for and 'b' for the next
a = input("What is the first temperature? ")
b = input("What is the second temperature? ")

#we convert 'a' into a string from an integer
a = str(a) 
b = str(b)

if a == b: 
    print(a + " and " + b + " are equal!")
else:
    print(a + " and " + b + " are NOT equal!")
