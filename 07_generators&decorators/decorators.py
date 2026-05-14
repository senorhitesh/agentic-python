def my_decorator(function):
    def wrapper():
        print("Before Function Runs")
        function()
        print("After Function Runs")

    return wrapper


@my_decorator
def greet():
    print("Hello")

greet()