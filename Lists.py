# Zain Kergaye
# Mr. Webster
# Programming 2
# 4/21/21

import os

lists = ['Burgers', 'Pizza', 'Shakes', 'Candy', 'Fries', 'Sandwhich', 'Salad', 'Fruit', 'Veggies', 'Water']

list2 = ['Dr. Pepper', 'Sprite', 'Coke', 'Lemonade', 'Pepsi']

for x in list2:
    lists.append(x)

print(lists)
os.system("pause")
print(len(lists))
os.system("pause")
print(type(lists))
os.system("pause")
for lists in lists:
    print(lists)
os.system("pause")
print(lists[2:5])
#os.system("pause")

