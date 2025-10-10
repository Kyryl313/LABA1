def track_history(func):
    history = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        history.append(result)
        history[:] = history[-5:]
        print(history)
        return result

    wrapper.history = history
    return wrapper
