num = int(input("Please enter a number"))
if num > 1:
    for i in range(2,num):
        if(num%2)==0:
            print(num,"is not prime number")
            print(i,"times",num//i ,"is",num)
            break
        else:
            print(num,"it is a prime number")
else:
   print(num,"is not a prime number")
