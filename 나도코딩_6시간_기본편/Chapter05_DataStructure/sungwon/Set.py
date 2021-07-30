#Set

my_set={1,2,3,3,3}
print(my_set)

java={'a', 'b', 'c'}
python=set(['c', 'e'])

print(java&python)
print(java. intersection(python))

print(java|python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add('f')
print(python)

java.remove('c')
print(java)