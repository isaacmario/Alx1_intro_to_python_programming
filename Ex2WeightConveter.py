weight = float(input("Enter your weight"))
unit = input("kilograms or pounds? (K or L)")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is: {round(weight , 1)} {unit}")
elif unit == "L":
    weight = weght/2.205
    unit = "Kgs"
    print(f"your weight is: {round(weight , 1)} {unit}")
else:
    print(f"{unit} was not valid")