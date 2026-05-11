tea_pries = {
    "Masala Chai": 40,
    "Green Chai": 100,
    "Lemon Chai" :10
}

conversion = {tea:price /80  for tea,price in tea_pries.items()}
print(conversion)