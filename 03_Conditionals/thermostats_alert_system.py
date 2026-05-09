device_status = True
current_temp = int(input("Enter Current Temp: "))

if device_status:
    if current_temp >35:
        print("Temp is very High")
    else:
        print("Normal Temperature")
else:
    print("Device is Off") 