from functools import reduce

# a,b,c = list(map(int,input().split()))
# print(a,b,c)

# A = list(map(lambda x: x ** 2, range(5))) 
# print(*A)

print(reduce(lambda x, y: y + x, 'abcde'))