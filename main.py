# BMI - (weight in pounds * 703)/(height in inches * height in inches)

name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your weight in inches: "))

BMI = (weight * 703) / (height * height)

match BMI:
    case BMI if BMI > 30:
        status = "Obese"
    case BMI if (30 > BMI >= 25):
        status = "OverWeight"
    case BMI if (25 > BMI >= 18.5):
        status = "Health Weight"
    case _:
        status = "UnderWeight"


print(name + f"'s BMI Calculation: {BMI:.2f} (" + status + ")")

if status == "UnderWeight":
    print("Kindly Eat more food")
elif status == "Obese" or status == "Overweight":
    print("Incorporate a diet")
else:
    print("Keep up the good work")
