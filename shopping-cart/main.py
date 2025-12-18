basket = {}
should_continue = True
print(" ")
print("\033[4mYOUR SHOPPING CART\033[0m")
print(" ")

while True:
    while True:
        new_item = str(input("Enter Item: ").lower())
        valid_input = True
        for letter in new_item:
            if not (letter.isalpha() or letter.isspace()):
                print(("ERROR: Item must be Alphabetical (e.g. Apples)"))
                valid_input = False
                break
        if valid_input == False:
            continue
        else:
            break

    while True:
        try:
            unit_price = float(input("Enter Item Price:"))
            if unit_price > 0:
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

    total = unit_price * qty

    basket[new_item] = {
        "unit_price":unit_price,
        "quantity": qty,
        "total": total
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


print(" ")
print(f"{'ITEM':<25} {'PRICE':^7} {'QTY':^6} {'TOTAL':>9}")
print("-" * 50)

for item in basket:
    column_one = item.capitalize()
    column_two = basket[item]["unit_price"]
    column_three = basket[item]["quantity"]
    column_four = basket[item]["total"]

    print(f"{column_one:<25}", end= " ")
    print(f"{column_two:>6.2f}", end= " ")
    print(f"{column_three:>5}", end= " ")
    print(f"{column_four:>11.2f}")

end_price = 0.0 

for item in basket:
    end_price = end_price + basket[item]["total"] 
print("-" * 50)
print(f"{'TOTAL':<42} {'£':}{end_price:>6.2f}")

