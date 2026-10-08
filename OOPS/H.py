class Car:
    wheels = 4
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color 
        
car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")

print(car1.brand)
print(car2.color)
print(car1.wheels)
print(car2.wheels)