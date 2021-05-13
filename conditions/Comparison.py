password = input("Enter a password here that has at least 3 characters but inter 11 characters: \n")

if len(password) < 3:
    print("Password must be at least 3 characters")
elif len(password) > 11:
    print("Password must be less than 11 characters")
else:
    print("Great looking password. It may not be easy to Hack you.")
