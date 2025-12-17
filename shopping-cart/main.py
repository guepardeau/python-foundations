basket = {}

print("YOUR SHOPPING CART")
print(" ")

while True:
    while True:
        item = str(input("Enter Item: ").lower())
        if item.isalpha():
            break
        else:
            print(("ERROR: Item must be Alphabetical (e.g. Apples)"))

    while True:
        try:
            price = float(input("Enter Item Price:"))
            if price > 0:
                break
            else:
                print("ERROR: Price must be greater than 0.") 
                continue
        except ValueError:
            print("ERROR: Price must be numerical: ")

    while True:
        try:
            qty = int(input("Enter Item Quantity: "))
            if qty > 0:
                break
            else:
                print("ERROR: Quantity must be greater than 0.") 
                continue
        except ValueError:
            print("ERROR: Quantity must be an integer (e.g. 4 for 4 apples): ")

    basket[item] = {
        "price":price,
        "quantity": qty
    }

    end_shopping = input("Would you like to add another item? (Y/N): ").upper()
    if end_shopping == "Y":
        continue
    elif end_shopping == "N":
        break
    else:
        print("ERROR: Please choose Y/N: ")

print(basket)
