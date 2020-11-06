a = int(input("Please enter a number"))
b = int(input("Please enter a number"))
c = int(input("Please enter a number"))
if a > b and a > c:
    print(a ,"is greatest number")
elif b > a and b > c:
    print(b,"is greatest number")
elif c > b and c > a:
    print(c," is greatest number")
else:
    print("Error")
