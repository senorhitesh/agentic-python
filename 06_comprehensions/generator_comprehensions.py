daily_sales = [1,2,3,4,5,6,7,8,9]

sales = (sale for sale in daily_sales if sale> 3)
print(sum(sales))