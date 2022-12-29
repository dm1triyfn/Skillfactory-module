per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('money = '))
deposit = []
for value in per_cent:
    deposit.append(per_cent[value]*money/100)
print(deposit)
deposit_max = max(deposit)
print('Максимальная сумма, которую вы можете заработать - ' + str(deposit_max))
