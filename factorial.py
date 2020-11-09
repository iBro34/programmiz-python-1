num = int(input("Please enter a number"))
fact = 1
if num < 0:
    print("Sorry it is 404")
elif num == 0:
    print(num ,"1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(num,"factorial is",fact)