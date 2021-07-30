#문자열 처리 함수

python="Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index=python.index("n")
print(index+1)
index=python.index("n", index+1)
print(index)

print(python.find("Java")) #존재하지 않을 시 -1을 반환
#print(python.index("Java")) Error

print(python.count("n"))
