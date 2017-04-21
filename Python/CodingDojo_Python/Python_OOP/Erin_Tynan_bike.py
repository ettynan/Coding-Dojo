class Bike:
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "This bike cost $", str(self.price), "has a max speed of", str(self.max_speed), "mph and has been ridden", str(self.miles), "miles."
      
    def ride(self):
        print "Ride"
        self.miles += 10
    
    def reverse(self):
        print "Reverse!"
        if self.miles >= 5:
            self.miles -= 5
            

bike1 = Bike(2000, 30, 100)
bike2 = Bike(20, 5, 30)
bike3 =Bike(100, 15, 50)

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
print bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
print bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
print bike3.displayInfo()