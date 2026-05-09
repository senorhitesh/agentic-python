order_chai = input("Enter your cup size (small/large/medium): ").lower()
cups = int(input("How many chai cups u want: "))
if order_chai == "small":
    print(f"your total price for small size : " , 10* cups, f"1 Cup = 10Rs (10 * {cups})" )
elif order_chai == "large":
    print(f"your total price for large size : " , 30* cups , f"1 Cup = 30Rs (10 * {cups})" )
elif order_chai == "medium":
     print(f"your total price for medium size : " , 60* cups , f"1 Cup = 60Rs (10 * {cups})" )
else:
    print("Invalid size")
