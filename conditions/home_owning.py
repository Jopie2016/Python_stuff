price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
    print("Buyer needs to put down 10%")
else:
    down_payment = 0.2 * price
    print("Buyer Needs to pay 20%")
print(f"Down payment: ${down_payment}")