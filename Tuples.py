#Zain Kergaye
#Mr. Webster
#Programming 2
#4/29/21

import os

tuple = ('apple', 'banana', 'pear', 'pineapple', 'cherry', 'orange')

os.system("pause")
print(tuple[1])
print(tuple[-1])
os.system("pause")

tuple = tuple + ('hamberger',)

os.system("pause")

for x in range(len(tuple)):
    print(tuple)

os.system("pause")

tuple.sort()
print(tuple)