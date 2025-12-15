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
time = input("How many years will the money be growing? (e.g 15 for 15 years): ")
time = get_valid_float(time)
applied_per_year = (input("How often will interest be paid out, daily, monthly or yearly?: "))
applied_per_year = applied_per_year.strip().lower()[0]
applied_per_year = get_valid_choice(applied_per_year, {"d","m","y"})



         