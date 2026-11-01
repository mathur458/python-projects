def calculate_total(price, tax):
    unused_value = 100
    total = price + (price * tax / 100)
    return total

print(calculate_total(1000, 18))
