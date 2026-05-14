def local_coffee():
    yield "Masala Coffe"
    yield "Cappecino";

def imported_coffee():
    yield "Lambren"
    yield "Brew";

def full_menu():
    yield from local_coffee()
    yield from imported_coffee();

for coffee in full_menu():
    print(coffee);

def chai_stall():
    print("Welcome to Our Tapri")
    try:
        order = yield
        yield f"Waiting for Order {order}"
    except:
        print("Tapri is Closed")

stall = chai_stall()
print(next(stall))
print(stall.send("Masala Chai"))
stall.close()
