user_weight = int(input("What is your weight: \n"))
weight_unit = input("type 'L' for (lbs) and 'K' for kg: \n")

if weight_unit.upper() == "L":
    converted_weight = user_weight * 0.45
    print(f"You are {converted_weight} kilos")
else:
    converted_weight = user_weight / 0.45
    print(f"You are {converted_weight} pounds")