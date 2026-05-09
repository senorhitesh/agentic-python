users =[ {"id":1,"name":"Hitesh","Profression":"Coder"},
        {"id":2,"name":"Bhavik","Profression":"Coder"},
        {"id":3,"name":"Aaditya","Profression":"Coder"}]

salary ={
    "Hitesh": (100000 , 0.10),
    "Bhavik" : (1000 , 0.20),
    "Aaditya" : (1200 , 0.40)
}

for user in users:
    salaryy,esops = salary.get(user['name'])
    if salaryy == None or esops == None:
        print("Error")
    print(f"Salary of {user['name']}  is {salaryy} & esop are {esops}")