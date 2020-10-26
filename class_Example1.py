class Rectangle: #capitalize the first letter of a class
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.top_left = (self.x, self.y)
        self.bottom_right = (self.x + self.width, self.y + self.height)
    
    def get_corners(self):
        top_left = (self.x, self.y)
        top_right = (self.x + self.width, self.y)
        bottom_left = (self.x, self.y + self.height)
        bottom_right = (self.x + self.width, self.y + self.height)
        corners = (top_left, top_right, bottom_left, bottom_right)
        return corners

    def collide_point(self, point):
        # returns true if the given point is in the Rectangle object
        # False otherwise
        within_x_range = point[0] >= self.x and point[0] <= self.x + self.width
        within_y_range = point[1] >= self.y and point[1] <= self.y + self.height

        #these are bound to bool

        if within_x_range and within_y_range: 
            return True
        else:
            return False

    def collide_points(self, points):
        # returns true if any of the point in points is in the Rectangle
        for point in points:
            if self.collide_point(point) == True:
            # we must add self before another function if we were to call it wihtin another function in the same class
                return True #quit method if true
        return False

    def collide_rect(self, other):
        # return True if the other rectangle overlaps the self
        # otherwise False
        self_on_left = self.bottom_right[0] < other.top_left[0]
        self_on_right = self.top_left[0] > other.bottom_right[0]
        self_on_top = self.bottom_right[1] < other.top_left[1]
        self_on_bottom = self.top_left[1] > other.bottom_right[1]
        if self_on_left or self_on_right or self_on_top or self_on_bottom:
            return False
        else:
            return True
    
def main():
    r1 = Rectangle(10, 20, 20, 10)
    r2 = Rectangle(50, 100, 200, 150)
    r3 = Rectangle(30, 40, 10, 20)
    corners = r1.get_corners() # this is a method call, there are no paramters (not even self)
    for corner in corners:
        print(corner)
    point1 = (101,201)
    point2 = (80,80)
    
    print("Testing collide_point")
    print(r1.collide_point(point1))
    print(r1.collide_point(point2))
    
    print("Testing collide_points")
    points = (point1, point2)
    print(r1.collide_points(points))

    print("***Test collide_rect method***")
    r1 = Rectangle(50, 50, 50, 50)
    r2 = Rectangle(200, 200, 50, 50)
    print(r1.collide_rect(r2))
    # software quality
    # innstance attirbutes of a class to be accessed or modified directly outside of the class
    # Violation of software quality - marks will be deducted
    # DON'T DO THIS
    
    

main()
    
        