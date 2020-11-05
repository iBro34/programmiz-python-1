import random
a = int(input("Please enter number to a"))

b = int(input("Please enter number to b"))

temp = a
a = b
b = temp
print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))
print(random.randint(0,100))