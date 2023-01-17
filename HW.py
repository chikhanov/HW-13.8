price = 0
while True:
    try:
        tickets = int(input('Сколько билетов вы хотите купить? '))
        if type(tickets) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(tickets):
    i += 1
    while True:
        try:
            age = int(input(f'Для какого возраста билет №{i}? '))
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                price += 990
                print('Стоимость билета: 990 руб.')
            else:
                price += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if tickets > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. с учетом 10%-ой скидки за регистрацию более 3-х билетов.')
