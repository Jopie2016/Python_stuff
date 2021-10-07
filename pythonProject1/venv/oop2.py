class Phone:
    def __init__(self, brand, price): #instatiates the object as it it created
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

iphone = Phone("Iphone 11", 600)
samsung = Phone("Galaxy S21", )
