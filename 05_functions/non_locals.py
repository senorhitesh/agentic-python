# To Change the Parnet Varible

def chai():
    chai_type = "Ginger"
    def change():
        nonlocal chai_type
        chai_type = "Lemon"
    change()
    print(f"{chai_type}")

chai()