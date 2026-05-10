# Scopes
# LOCAL SCOPES - Inside an Function # Enclosing -   from outer functions if nested # Global - Top Level Script

def serve_chai():
    chai_type = "Masala Chai" # local scopes
    print(f"Chai inside is {chai_type}");

chai_type = "Lemon Chai"
print(f" Chai Outside  {chai_type}")



def chai_counter():
    chai_order = "Gingerr" # Enclosing Scope
    def  print_order():
        print(f"Inner: {chai_order}");
    print_order()
    print(f"Outer: {chai_order}")

chai_order = "No Chai"

chai_counter()
print(f"Global: {chai_order}")
