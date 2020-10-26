# this program determines the location of a coordinate based on user inputs for (x,y).

# this function pinpoints the location of the coordinate based on the value of x and y
def quadrant_determination(x,y, coordinate):
    if x > 0 and y > 0:
        print("The point (" + coordinate + ") lies in Quadrant I")
    elif x < 0 and y > 0:
        print("The point (" + coordinate + ") lies in Quadrant II")
    elif x < 0 and y < 0:
        print("The point (" + coordinate + ") lies in Quadrant III")
    elif x > 0 and y < 0:
        print("The point (" + coordinate + ") lies in Quadrant IV")
    elif x == 0 and (y < 0 or y > 0):
        print("The point (" + coordinate + ") lies on a border between two quadrants.")
    elif (x < 0 or x > 0) and y == 0:
        print("The point (" + coordinate + ") lies on a border between two quadrants.")
    else:
        print("The point (0, 0) lies at the origin.")

def get_xy():
    x = int(input("Input the value for the X coordinate: "))
    y = int(input("Input the value fot the Y coordinate: ")) 
    return x, y

def point(x, y):
    x = str(x)
    y = str(y)

    coordinate = x + ',' + y
    return coordinate

def main():
    x, y = get_xy()
    coordinate = point(x, y)
    quadrant_determination(x,y, coordinate)

main()