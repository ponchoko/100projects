def main():
    weight = int(input("What is your weight in kg?: "))
    height = float(input("What is your height in cm?"))
    bmi = weight / (height * height)
    print(bmi)
    if bmi < 18.5:
        print("Underweight")
    elif bmi <25:
        print("Healthy")
    elif bmi <30:
        print("Overweight")
    elif bmi >= 30:
        print("Obese")
    exit
    
main()