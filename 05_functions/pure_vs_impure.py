def recursion(m):
    print(m)
    if(m ==0):
        return;
    return recursion(m - 1)

recursion(100)

chai_types = ["Light", "Kadak", "Masala", "Looser" ,"Looser"]
chai_types = ["Light", "Kadak", "Masala", "Looser" ,"Looser"]


strong_chai = list(filter(lambda chai: chai != "Looser",  chai_types))
print(strong_chai)