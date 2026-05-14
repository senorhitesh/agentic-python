from functools import wraps
def log_activity(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling Function {func.__name__}")
        result = func(*args,**kwargs)
        return result
    return wrapper

@log_activity
def brew_chai(type):
    print(f"Making your {type}")

brew_chai("Masala Chai")