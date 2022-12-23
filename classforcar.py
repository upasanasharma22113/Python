# instance variables--value varies object to object
# static variable----values same 

class car:
    wheel=4
    def __init__(self):
        self.company="BMW"
        self.mileage=10
        car.wheel=5
car1=car()
car2=car()
print(car1.mileage, car1.wheel)
print(car2.mileage,car2.wheel)
print(car.wheel) # another way

