from decorator import track_history
@track_history
def numbers(a, b):
    return a + b
numbers(0, 1)
numbers(0,2 )
numbers(0, 3)
numbers(0, 4)
numbers(0, 5)
numbers(0, 6)
