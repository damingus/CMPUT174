temp = input("Input the temperature: ")

if temp <= 0:
    print("The temperature is freezing!")
elif temp > 0 and temp < 10:
    print("The temperature is cold!")
elif temp >= 10 and temp < 20:
    print("The temperature is chilly!")
elif temp  >= 20 and temp < 30:
    print("The temperature is warm!")
elif temp >=30 and temp < 40:
    print("The temperature is hot!")
else:
    print("The temperature is extremely hot!")