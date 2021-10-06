x = 0

while x < 10:
    x += 1
    if x == 7: # skips 7 but keeps going
        continue
    print(x)

i = 10

while 10 >= i > 0:
    if i % 2 == 0:
        print(f"{i} is divisible by 2")
    else:
        print(f"{i} is not divisible by 2")
    i -= 1

v = 5

while v >= 0:
    if v == 0:
        print("GO!")
    else:
        print(v)
    v -= 1