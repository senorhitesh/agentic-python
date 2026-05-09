order_amount = int(input("Enter your Order Amount: "))

delivery_fees = 0 if order_amount > 300 else 30;

print(f"Your Total Price is {order_amount + delivery_fees} as delivery fees is {delivery_fees}")