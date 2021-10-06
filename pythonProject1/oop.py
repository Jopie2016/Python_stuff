class Person:
    def __init__(self, name, age, weight):  # Two properties of this class is name and age
        self.name = name
        self.age = age
        self.weight = weight

    def walk(self):  # Self allows us to get access to the properties above
        print(self.name + " Is walking...")

    def speak(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old")

    def workout(self):
        print("My goal weight is " + str(self.weight) + " lbs")


john = Person("John", 22, 205)
john.speak()
john.walk()
john.workout()


print("------------------------------")


bob = Person("Bob", 29, 200)
bob.speak()
bob.walk()
bob.workout()
