#ask for user input of (x, y) and convert to integer class
x = int(input("Input the value for the X coordinate: "))
y = int(input("Input the value for the Y coordinate: "))

#set string_xy 
string_xy = str(x) + ', ' + str(y)

def main():
    if x > 0 and y > 0: #
        print("The point (" + string_xy + ") lies in Quadrant I")
    elif x < 0 and y > 0:
        print("The point (" + string_xy + ") lies in Quadrant II")
    elif x < 0 and y < 0:
        print("The point (" + string_xy + ") lies in Quadrant III")
    elif x > 0 and y < 0:
        print("The point (" + string_xy + ") lies in Quadrant IV")
    else:
        print("The point (0, 0) lies at the origin.")

main()