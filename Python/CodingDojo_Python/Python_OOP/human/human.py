class Human(object):
    def __init__(self):
        print "New Human!!!"
    def taunt(self):
        print "You wanna piece of me?"
Michael = Human()
Jimmy = Human()

Michael.taunt()
print Jimmy

class Point(object):
    def __init__(self, x = 0, y = 0):
        print "Created a new point!"
        self.x = x
        self.y = y
    def distance(self):
        #find distance from origin
        return (self.x**2 + self.y**2) ** 0.5

class Cat(object):
    pass
