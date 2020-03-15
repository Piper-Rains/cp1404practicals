total = 0
num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid item number")
    num_items = int(input("Number of items: "))

for i in range(num_items):
    price = float(input("Price of item: "))
    total = total + price
if total > 100:
    total = total*0.9
print("Total price for " + str(num_items) + " is $" + str(total))
