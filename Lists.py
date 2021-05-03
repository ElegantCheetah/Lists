# Zain Kergaye
# Mr. Webster
# Programming 2
# 4/21/21

import os

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [11, 12, 13, 14, 15]

for x in list2:
    lists.append(x)

print(lists)

os.system("pause")

print(len(lists))

os.system("pause")

print(type(lists))

os.system("pause")

for lisxts in lists:
    print(lisxts)

os.system("pause")

print(lists[3])

os.system("pause")

y = 0
for x in lists:
    y+=1
    print(str(y) + '. ' + x)

for list2, x in enumerate(lists):
    print (lists, x)
