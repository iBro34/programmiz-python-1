num = int(input("Please enter a number"))
    if num > 1:
        for i in range(2,num):
            if(num%2)==0:
                print(num ,"is not a prime a number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is prime number")
    else:
        print("Error")
    