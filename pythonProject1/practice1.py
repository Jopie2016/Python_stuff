age = int(input("Enter your age"))

if age:
    if 18 <= age < 21:
        print("You can enter, but you need a band")
    elif age >= 21:
        print("Enter my friend")
    else:
        print("You can't enter")
else:
    print("you cant enter in")
