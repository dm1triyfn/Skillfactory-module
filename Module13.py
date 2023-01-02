number_of_ticket = int(input('Введите кол-во билетов - '))
ages = []
for i in range(1, number_of_ticket + 1):
    age = int(input(f'Введите возраст для билета {i} - '))
    ages.append(age)

money = 0
for age in ages:
    if 1 <= age < 18:
        money += 0
    elif 18 <= age < 25:
        money += 990
    elif age >= 25:
        money += 1390

if number_of_ticket > 3:
    money = money * 0.9
print(f'Стоимость со скидкой - {money}')

