import statistics

a = input("What is the first temperature? ")
b = input("What is the second temperature? ")
c = input("What is the third temperature? ")

list = [a, b, c]
median = statistics.median(list)
print("The middle number was ", median)
     