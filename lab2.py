house_price = 1000000

name = input("What is your name? ")
print(f"Hello {name}")
amount = str(input("How much is your budget? "))
print(f"You have {amount} as your budget")
if int(amount) > 500000:
        print("Your down payment is", (20 / 100) * house_price)
elif int(amount) >= 300000 and int(amount) < 500000:
        print("Your down payment is", (10 / 100) * house_price)
else:
    print(f"Your amount {amount} is not enough to buy a house")
        
