class BaseChai:
    def __init__(self,type_) -> None:
        self.type = type_

    def prepare(self):
        return f"Preparing {self.type} ..........................................";

chai = BaseChai("Masala Chai")

print(chai.prepare())

# for Inheritance

class MasalaChai(BaseChai):

    def add_species(self):
        return f"Adding Cardom, ginger, cloves"
    

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self) -> None:
        self.chai = self.chai_cls("Regular Chai")

    def serve(self):
        print(f"Serving {self.chai}")
        self.chai.prepare();

class FancyChai(ChaiShop):
    chai_cls = MasalaChai;



shop = ChaiShop();
fancy  = FancyChai();

shop.serve()