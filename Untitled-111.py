
# Розрахунок вартості замовлення зі знижкою

try:
    total = float(input("Введіть суму покупки (грн): "))

    if total <= 0:
        print("Помилка! Сума покупки повинна бути більшою за 0.")

    elif total < 1000:
        discount = 0

    elif total < 3000:
        discount = 5

    elif total < 5000:
        discount = 10

    else:
        discount = 15

    if total > 0:
        savings = total * discount / 100
        final_price = total - savings

        print("Сума покупки:", total, "грн")
        print("Знижка:", discount, "%")
        print("Економія:", savings, "грн")
        print("До сплати:", final_price, "грн")

except ValueError:
    print("Помилка! Потрібно вводити числове значення.")
