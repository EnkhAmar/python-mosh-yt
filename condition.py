price_house = 1000000
good_credit = False

if good_credit:
    downpayment = price_house * 0.1
else:
    downpayment = price_house * 0.2

print(f"Down payment: ${downpayment}")