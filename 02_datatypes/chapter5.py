import sys
from fractions import Fraction
from decimal import Decimal
is_boiling = True
total = (is_boiling) + 100
# print(total , type(total))

a = 22.01
b = 33.022222

print(Decimal(a) + Decimal(b))

# print only 2 decimal places after addition
result = Decimal(a) + Decimal(b)
print(result.quantize(Decimal('0.001')))