from compound import compound

def get_valid_float(user_input):
            while True:
                try: 
                    user_input = float(user_input)
                    return user_input
                except ValueError:
                    user_input = ((input(f"{user_input} must be a numerical value.")))

def get_valid_choice(user_input, allowed_choices):
      while True:
            if user_input in allowed_choices:
                  return user_input
            else:
                  user_input = input(f"{user_input} is not valid. Please try again. ")

currency = (input("Which currency are you using ($/£/€)?: "))
currency = get_valid_choice(currency, ["$", "£","€"])
principal = ((input("Please enter starting balance. (e.g 10000): ")))
principal = get_valid_float(principal)
interest_rate = (input("Please enter the interest rate (e.g 2.5): "))
interest_rate = get_valid_float(interest_rate)
interest_rate = interest_rate/100

while True:
   try:
        time = float(input("How many years will the money be growing? (e.g 15 for 15 years): "))
        if time > 0:
            break
        else:
            print("You cannot have negative years. Enter a number greater than 0: ")
   except ValueError:
        print("Time must be numerical.")

while True:
    applied_per_year = (input("How often will interest be paid out, daily, monthly or yearly?: ").strip().lower())
    if applied_per_year in ["daily", "monthly", "yearly"]:
        break
    else:   
        print(f"{applied_per_year} is not valid.")

if applied_per_year == "daily":
      applied_per_year = 365
elif applied_per_year == "monthly":
      applied_per_year = 12
elif applied_per_year == "yearly":
      applied_per_year = 1
else:
      pass

amount = compound(principal, interest_rate, applied_per_year, time)
difference = amount - principal
growth_factor = (amount/principal)
growth_percentage = (growth_factor-1)*100

print(f"The final amount after {time} years would be {currency}{amount:.2f}. You would earn {currency}{difference:.2f}. A growth of {growth_percentage:.2f}%.")



         