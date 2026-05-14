def cahi_customers():
    print("Welcome Sir Ji , What would u like to prefer")
    order = yield
    while True:
        yield f"we are preparing {order}"
        order = yield;

order = cahi_customers()
print(next(order))
print(order.send("Chai Garam Garam"))