def currency_conversion(amount):
    rates = {"INR": 82.5, "EUR": 0.92, "GBP": 0.78}
    return {currency: amount * rate for currency, rate in rates.items()}

usd_amount = float(input("Enter the amount in USD: "))
converted = currency_conversion(usd_amount)
for currency, value in converted.items():
    print(f"{usd_amount} USD = {value:.2f} {currency}")