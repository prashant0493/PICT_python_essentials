def bmi(weight, height):
    return weight / height**2


def bmi_evaluate(bmi_value):
    if bmi_value < 15:
        print("underweight")
    elif bmi_value < 25:
        print("normal")
    else:
        print("overweight")


bmi_res = bmi(70, 1.76)

print(bmi_res)
bmi_evaluate(bmi_res)
