import random
from datetime import date

# hypotenuse  =  int(input("Enter your triange Hypotenuse"))
# base =  int(input("Enter your triange Base"))
# perpendicular  = int(input("Enter your triange Perpendicular"))


# if hypotenuse == base == perpendicular:
#     print(f"Your trainge is Equalilatral as {hypotenuse} == {base} == {perpendicular} ")
# elif hypotenuse == base or base == perpendicular or hypotenuse == perpendicular:
#     print(f"Your Triange is Isosceles as Two Sides are Equal")
# elif hypotenuse != base != perpendicular:
#     print("Your Triange is Scalene")


# d1 = int(input("Enter Year"))
# datee = date(d1,1,1)
# datee2 = date(d1+1, 1, 1)
# diff = datee2 - datee

# if(diff == 366):
#     print(f"It's a Leap Year Man {d1}")
# else:
#     print("No Leap Year")



# unit_consumed = int(input("Enter Unit"));
# if unit_consumed <= 100:
#     total_bill1 = unit_consumed * 5
#     print(total_bill1)

# numb = int(input("Enter Number"))

# if numb > 0:
#     print("Number is Positive");
#     if numb % 2 == 0:
#         print("Numb is Even")
#     else:
#         print("Number is Odd")
#     if numb % 15 == 0:
#         print("NUmber is divisibble by 3 and 5")
#     else:
#         print("NUmber is not divisibble by 3 and 5")
        
# else:
#     print("Number is Negative")




moves = ["Rock", "Paper", "Scissors"]

player_move = random.choice(moves)
computer_move = random.choice(moves)

print("Player:", player_move)
print("Computer:", computer_move)

if player_move == computer_move:
    print("It's a Draw")

elif (
    (player_move == "Rock" and computer_move == "Scissors") or
    (player_move == "Paper" and computer_move == "Rock") or
    (player_move == "Scissors" and computer_move == "Paper")
):
    print("Player Wins")

else:
    print("Computer Wins")
    
unit = int(input("Enter Units: "))

if unit <= 100:
    bill = unit * 5

elif unit <= 200:
    bill = (100 * 5) + ((unit - 100) * 8)

else:
    bill = (100 * 5) + (100 * 8) + ((unit - 200) * 10)

print("Total Bill:", bill)