class Phone:
    def __init__(self, brand, price): #instatiates the object as it it created
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

    def __str__(self) -> str: #Overides string method
        return f"Brand = {self.brand}\nPrice = {self.price}"


iphone = Phone("iphone 11", 600)
samsung = Phone("Galaxy S21", 1000)

iphone.call("718-359-8753")
print(samsung.price)

print(iphone)
print(samsung)

