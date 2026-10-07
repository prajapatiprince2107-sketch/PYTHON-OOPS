class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("My name is", self.name,
              "I am", self.age,
              "years old and I study", self.course)


student1 = Student("Prince", 20, "Data Science")
student2 = Student("Nox", 22, "Cyber Security")

student1.introduce()
student2.introduce()