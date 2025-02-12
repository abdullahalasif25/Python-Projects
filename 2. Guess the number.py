import random
a = int(input("Enter a number: "))
b = random.randint(1, a)
c= int(input("Try a number: "))
while c!=b:
    if c>b:
        print("Too high")
    else:
        print("Too low")
    c= int(input("Try a number: "))

print("You are right!")
