weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if (unit == 'K' or unit == 'k'):
    weight = weight * 2.20462
    unit = 'kilograms'
elif (unit == 'L' or unit == 'l'):
    weight = weight * 0.453592
    unit = 'pounds'

print(f"You are {weight} {unit}")