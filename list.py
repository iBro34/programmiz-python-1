sales_w1 = [21,3,43,12,2,4,5]
sales_w2 = [34,4,32,12,7,15]
new_day = input("Please enter #of lemons for a day")
sales = sales_w1 + sales_w2
worst_day = min(sales)*1.5
best_day = max(sales)*1.5
commit = worst_day + best_day
print("The worst day profit:$",worst_day)
print("The best day profit:$",best_day)
print("Combination:$",commit)