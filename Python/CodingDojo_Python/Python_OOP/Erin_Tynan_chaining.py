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
        return self
    
    def reverse(self):
        print "Reverse!"
        if self.miles >= 5:
            self.miles -= 5
        return self
            

bike1 = Bike(2000, 30, 100)
bike2 = Bike(20, 5, 30)
bike3 =Bike(100, 15, 50)

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()