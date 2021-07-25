from random import *

print(random())
print(random()*10)
print(int(random()*10))
print(int(random()*10)+1)

first_num=1
last_num=45

print(int(random()*last_num)+first_num)
print(randrange(first_num,last_num+1)) #last_num미만의 수 까지
print(randint(first_num, last_num))