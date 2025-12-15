def compound (principal, interest_rate, applied_per_year,time):
    amount = (principal * (1+interest_rate/applied_per_year)**(applied_per_year*time))
    return amount