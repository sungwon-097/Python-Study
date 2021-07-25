#List

subway=[10,20,30]
print(subway)

subway=['a', 'b', 'c']
print(subway.index('b'))

subway.append('d')
print(subway)

subway.insert(1,'d')
print(subway)

print(subway.count('d'))

print(subway.pop())
print(subway)

num_list=[5,2,4,3,1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

mix_list=[1,2,3,True, "Sungwon"]
print(mix_list)

num_list.extend(mix_list)