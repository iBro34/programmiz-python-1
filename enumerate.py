print('python101 - enumerate')
friends = ["ikhtiyar","Sunnat","Jasur","Abbos"]
i = 1
for friend in friends:
     print(i,friend)
     i= i+1
for num,friend in enumerate(friends):
    print(num,friend)