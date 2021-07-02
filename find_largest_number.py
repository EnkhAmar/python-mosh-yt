numbers = [1, 4, 5, 1, 3, 3]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print(f"Max: {max}")