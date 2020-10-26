#This program pinpoints what quandrant a point lies in after asking ther user for 'x' and 'y' into (x,y)

#We obtain an integer value for 'x' and 'y' by asking the user to input their values.
x = input("Input the value for the X coordinate: ")
y = input("Input the value for the Y coordinate: ")

#Depending on the positivity and negativity of 'x' and 'y', we can determine the quadrant they lie on.



if x > 0 and y > 0:
    print("The point (" + str(x) + ', ' + str(y) + ") lies in Quadrant I")
elif x < 0 and y > 0:
    print("The point (" + str(x) + ', ' + str(y) + ") lies in Quadrant II")
elif x < 0 and y < 0:
    print("The point (" + str(x) + ', ' + str(y) + ") lies in Quadrant III")
elif x > 0 and y < 0:
    print("The point (" + str(x) + ', ' + str(y) + ") lies in Quadrant IV")
else:
    print("The point (0, 0) lies at the origin.")
