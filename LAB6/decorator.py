def track_history(func):
    history = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        history.append(result)
        history[:] = history[-5:]
        print(history) #(на всякий випадок) замінити на history але тоді буде рез1 + рез2
        return result

    wrapper.history = history
    return wrapper
