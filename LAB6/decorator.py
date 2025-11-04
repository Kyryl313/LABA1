def track_history(func): #приймає нашу функцію (func)
    history = []

    def wrapper(a, b):
        result = func(a, b) #виклик ориг. функції і зберігаємо результат як result
        history.append(result)
        if len(history) > 5:
            history.pop(0)
        print(history)
        return result #повертаємо результат, щоб функція працювала як звичайно.

    return wrapper #повертаємо внутрішню функцію, бо її викликатиме
