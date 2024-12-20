def electricity_bill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        return 100 * 1.5 + 100 * 2.5 + (units - 200) * 4.0
    else:
        return 100 * 1.5 + 100 * 2.5 + 100 * 4.0 + (units - 300) * 5.0

units_consumed = int(input("Enter the number of units consumed: "))
print(f"Your electricity bill is: {electricity_bill(units_consumed):.2f}")