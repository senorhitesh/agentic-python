def secret_key():
    print("Secret Class")

def login(name, password):
    if (crendentials := name == "Hitesh" and password == 123):
        secret_key();
    else:
        print("Wrong Crenditials")
        return;
    
    print("Process Compelte")

login("Hitesh", 123)