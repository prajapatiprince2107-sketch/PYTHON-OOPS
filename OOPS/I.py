class Employee:
    company = "google"

    def __init__(self,name):
        self.name = name
    
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

print(Employee.company)

Employee.change_company("zometo")

print(Employee.company)