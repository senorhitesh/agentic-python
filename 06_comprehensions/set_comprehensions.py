menu = ["Masala Chai","Lemon Tea","Masala Chai" ,"Tinder Chai","Elachi Chai" ,"Lemon Tea"]

unqiue_chai = {chai for chai in menu }
print(unqiue_chai)

recipes = {
    "Paneer Bhurji" : ["Raw Panner", "Masala", "Water"],
    "Sev Tamatar" : ["Ratlami Sev", "Water", "Masala"],
    "Dal Bati" : ["Aata", "water"]
}

best = { specie for ingridents in recipes.values() for specie in ingridents}
print(best)