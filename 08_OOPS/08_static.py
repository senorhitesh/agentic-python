# class ChaiUtils:
#     @staticmethod
#     def clean_ingridents(text):
#         return [item.strip() for item in text.split(",")];

# raw = "   water, milk , aanag"

# print(ChaiUtils.clean_ingridents(raw))


# ClassMethod vs StaticMethod

class ChaiOrder:
    def __init__(self, type_, sweetness,size) -> None:
        self.type = type_
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dec(cls,order_data):
        return cls(
            order_data["type_"],
            order_data["sweetness"],
            order_data["size"],
        )
    @classmethod
    def from_string(cls, order_string):
        type_, sweetness, size = order_string.split("-")
        return cls(type_, sweetness, size);



order1 = ChaiOrder.from_dec({"type_":"Masala", "sweetness":"Sweetest","size":"Big"})
print(order1.__dict__)

order2 = ChaiOrder.from_string("Ginger-Sweet-Low")
print(order2.__dict__)

order3 = ChaiOrder("M","3",3)

print(order3.__dict__)
