print('Calculate an Adult BMI')

def bmi_input():
    name = input('Please enter your name: ')
    weight = float(input('Please enter your weight (in kg): '))
    height = float(input('Please enter your height (in m): '))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        weight_status = 'Underweight'
    elif 18.5 <= bmi < 25:
        weight_status = 'Healthy Weight'
    elif 25 <= bmi < 30:
        weight_status = 'Overweight'
    else:
        weight_status = 'Obesity'
    print(f'Hello {name}, your bmi is {bmi:.2f} and your weight status is {weight_status}')

bmi_input() 

def bmi(name, weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        weight_status = 'Underweight'
    elif 18.5 <= bmi < 25:
        weight_status = 'Healthy Weight'
    elif 25 <= bmi < 30:
        weight_status = 'Overweight'
    else:
        weight_status = 'Obesity'
    return f'Hello {name}, your bmi is {bmi:.2f} and your weight status is {weight_status}'

print(bmi('John', 76, 1.8))
print(bmi('James', 65, 1.72))