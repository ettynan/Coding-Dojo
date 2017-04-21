class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

        if (self.price> 10000):
            self.tax = .15
        else:
            self.tax = .12

        if (self.fuel < 100):
            self.fuel = "Full"
        elif(self.fuel < 100 and self.fuel >90):
            self.fuel = "Kind of Full"
        elif(self.fuel == 0):
            self.fuel = "Empty"
        else: 
            self.fuel = "Not full"

    def displayInfo(self):
        print "Price:", str(self.price)
        print "Speed:", str(self.speed), "mph"
        print "Fuel", (self.fuel)
        print "Mileage:", str(self.mileage), "mpg"
        print "Tax:", str(self.tax)

car1 = Car(2000, 35, 100, 15)
car2 = Car(2000, 5, 50, 105)
car3 = Car(2000, 25, 95, 25)
car4 = Car(2000, 15, 100, 50)
car5 = Car(2000, 45, 0, 25)
car6 = Car(2000000, 35, 0, 15)

car1.displayInfo()
car2.displayInfo()
car3.displayInfo()
car4.displayInfo()
car5.displayInfo()
car6.displayInfo()
