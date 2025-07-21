print("admission in golf club")

age = int(input("Enter your age: "))

if age < 25:
    print("You are too young to join the golf club.")

elif (age >= 30 ):
    print("You allowed to join the golf club.")

elif (age >= 40 ):
     print("You are too old to join the golf club.")
     
else:
    print("You are allowed to join the golf club, but you need to pay a higher fee.")