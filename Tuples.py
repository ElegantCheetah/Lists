#Zain Kergaye
#Mr. Webster
#Programming 2
#4/29/21

import os

tuple = ('apple', 'banana', 'pear', 'pineapple', 'cherry', 'orange')

def Reverse(tuple):
    new_tup = tuple[::-1]
    return new_tup

print(tuple[1])
print(tuple[-1])

os.system("pause")

tuple = tuple + ('hamberger',)
print(sorted(tuple))

os.system("pause")

#tuple.sort()
print(Reverse(tuple))

os.system("pause")

print('The min is ', min(tuple))
print('The max is ', max(tuple))