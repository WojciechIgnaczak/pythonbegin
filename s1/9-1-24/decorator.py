
def my_decorator(func):
    def wrapper():
        print("Tekst przd funkcaj")
        func()
        print("Teskt po wykonaniu funkcji")
    return wrapper

@my_decorator
def czesc():
    print("Hello world")
    
czesc()