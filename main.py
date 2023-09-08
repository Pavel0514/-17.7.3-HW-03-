per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму, которую планируете положить под проценты: "))

deposit = []
for bank, percent in per_cent.items():
    accrued_interest = money * percent / 100
    deposit.append(accrued_interest)

max_deposit = max(deposit)  # Находим максимальное значение в списке deposit

print("Накопленные средства за год вклада:")
for i, value in enumerate(deposit):
    print(f"Банк: {list(per_cent.keys())[i]}, сумма: {value:.2f}")

print(f"Максимальная сумма, которую вы можете заработать: {max_deposit:.2f}")