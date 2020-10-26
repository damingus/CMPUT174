class Dog:

    def __init__(self, breed, size):
        self.breed = breed
        self.size = size
        print(type(self))
    def bark(self):
        sound = self.breed + " barks, "
        if self.size == 'small':
            sound = sound + "yip yip"
        elif self.size == 'medium':
            sound = sound + 'woof woof'
        else:
            sound = sound + "BARK BARK"
        return sound
    

dog1 = Dog('doodle', 'small')
dog2 = Dog("German Shepard", 'large')

print(dog2.bark())

print(dog1.bark())
