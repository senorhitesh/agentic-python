class ChaiOrder:
    def __init__(self, type_, size , name) -> None:
        self.type = type_
        self.size = size
        self.c_name = name
    
    def summary(self):
        return f"{self.size}ml of size is required for {self.type} chai by customer {self.c_name}";

order = ChaiOrder("Masala", 200 , "Hitesh")
print(order.summary())

order2 = ChaiOrder("Ginger",210 , "Rahul");
print(order2.summary())