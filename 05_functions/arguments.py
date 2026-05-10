chai = "Lemon"
def prepare_chai(order):
    print("Preparing Order ", order)


val = [1,11,1]
def change(cal):
    cal[1] = 1000
change(val)
# print(val)



def  special(*ingredients, **extras):
    print("Ingri", ingredients)
    print("Extras", extras)
    
special("Ingri1","Ingri2" , extra1= "Elachi",extra2= "Bhaago", extra3= "Bala bali")
