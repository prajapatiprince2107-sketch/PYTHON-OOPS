class Cars:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
Car1 = Cars("Toyota", "Fortuner")
Car2 = Cars("bmw","x5")

print(Car1.brand)
print(Car1.model)
print(Car2.brand)
print(Car2.model)