basket = {}
should_continue = True

print("YOUR SHOPPING CART")
print(" ")

while True:
    while True:
        new_item = str(input("Enter Item: ").lower())
        if new_item.isalpha():
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

    basket[new_item] = {
        "price":price,
        "quantity": qty
    }
    end_shopping = None

    end_shopping = input("Would you like to add another item? (Y/N): ").upper()
    while True:
        if end_shopping == "Y" or end_shopping == "YES":
            break
        elif end_shopping == "N" or end_shopping == "NO":
            should_continue = False
            break
        else:
            end_shopping = input("Please choose (Y/N):" ).upper()
            continue
    
    if should_continue:
        continue
    else:
        break

for item in basket:
        print(item.capitalize(), end=" ")
        print(basket[item]["price"], end= " ")
        print(basket[item]["quantity"])


