from timer import counter

user_input = None
validated_input = None

while True:
    user_input = (input("How many seconds would you like to countdown from?: "))
    try:
        validated_input = int(user_input)
        if validated_input > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print(f"{user_input} is not valid. Please enter an integer above 0.")

(counter(validated_input))
print("Time's up.")
