successful = False
for number in range(3):
    print("Try", number + 1)
    if successful:
        print("Success")
        break
else:
    print("Attempted 3 times and failed")

sum_of_loop = 0
for x in range(3, 6): # 3-5 it stops at 6
    sum_of_loop += x
    print(sum_of_loop)
    # 0 + 3 = 3
    # 3 + 4 = 7
    # 7 + 5 = 12

co_workers = ["Tom", "Shirley", "Matias", "Alan"]
for x in co_workers:
    if x == "Tom":
        print("What's up Tom")
    elif x == "Shirley":
        print("What's up Shirley")
    elif x == "Matias":
        print("What's up Matias")
    else:
        print("What's up Alan")

lists = [1, 2, 3, 4, 5, 6, 7, 8]

for x in lists:
    if x == 3 or  x == 7:
        continue
    print(x)


