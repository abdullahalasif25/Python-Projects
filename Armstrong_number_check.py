number  = 153
n = number

result = 0
d = len(str(n))
while n>0:
    x = n%10
    n = n//10
    result = result + x**d

if result == number:
    print("Armstrong")
else:
    print("Not Armstrong")


