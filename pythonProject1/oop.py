class Person:
    def __init__(self, name, age):  # Two properties of this class is name and age
        self.name = name
        self.age = age

    def walk(self):  # Self allows us to get access to the properties above
        print(self.name + " Is walking...")

    def speak(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old")


john = Person("John", 22)
john.speak()
john.walk()


print("------------------------------")


bob = Person("Bob", 29)
bob.speak()
bob.walk()
