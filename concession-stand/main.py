def display_menu():
    menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
    print()
    print("-----------MENU-----------")
    for key, value in menu.items():
        print(f"{key:19}: £{value:.2f}")
    print("--------------------------")
    print(" ")
    return menu

def get_order(menu):
    cart = []    
    while True:
        food = input("Select an item: (q to quit): ").lower().strip()
        if food == "q":
            break
        elif menu.get(food) is not None:
            cart.append(food)
        elif menu.get(food) is None:
            print("We don't sell that, Sorry.")
            continue
    return cart

def calculate_total(cart, menu):
    total = 0
    for food in cart:
        total += menu.get(food)
    return total

def final_output(order_total):
    print()
    print(f"Your order comes to £{order_total:.2f}")
    print()

menu = display_menu()
cart = get_order(menu)
order_total = calculate_total(cart,menu)
final_output(order_total)