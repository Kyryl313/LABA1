def main():
    store = {
        "Стіл": 1500,
        "Стілець": 500,
        "Лампа": 400,
        "Шафа": 3200,
        "Диван": 5800}

    while True:
        choice = input("Оберіть дію (1 - Купити, 2 - Переглянути ціни): ")

        if choice == "1":
            order = input("Введіть товари через пробіл: ").split(" ")
            total = 0
            okay = True

            for item in order:
                item = item.strip()
                if item in store:
                    print(f"{item}: {store[item]} грн") #'f' дозволяє в рядку писати змінні чи вирази у { }
                    total += store[item] #оскільки тотал спочатку 0 то "+=" додає і присвоює йому значення
                else:
                    print(f"Немає товару: {item}")
                    okay = False

            if okay:
                print("Загальна сума:", total)
            else:
                print("Замовлення скасовано - деяких товарів немає.")

        elif choice == "2":
            print("Асортимент магазину:")
            for name, price in store.items():
                print(name, "-", price, "грн")
        else:
            print("Невірна опція!")

if __name__ == '__main__':
    main()