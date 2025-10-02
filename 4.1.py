def format_price(price): #Функція1 - формат ціни
    return f"{price:.2f} грн"

def check_availability(store, *items): #Функція2 - чек наявності
    return {item: store.get(item, [0, False]) for item in items} #get - Returns the value of the specified key

def order(store): #Функція3 - замовлення
    order = input("Введіть товари через пробіл: ").split()
    check = check_availability(store, *order)

    unavailable = [item for item, data in check.items() if not data[1]] #data[1] це II-елемент списку тобто наявність

    if unavailable:
        print("Замовлення скасовано! Немає:", ", ".join(unavailable)) #join обєднує в рядок через ", "
        return

    total = 0
    print("Замовлення:")
    for item, (price, available) in check.items():
        print(f"{item}: {format_price(price)}")
        total += price
    print("Загалом:", format_price(total))

def main():
    store = {
        "Стіл": [1500, True],
        "Стілець": [500, False],
        "Лампа": [400, False],
        "Шафа": [3200, True],
        "Диван": [5800, True]}

    while True:
        choice = input("Оберіть дію (1 - Купити, 2 - Переглянути ціни):")

        if choice == "1":
            order(store)

        elif choice == "2":
            for item, (price, available) in store.items():
                status = "+" if available else "-"
                print(f"{item}: {format_price(price)} ({status})")

        else:
            print("Непрописаний варіант!")

if __name__ == '__main__':
    main()
