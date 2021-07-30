#Dictionary

cabinet={3:"Jaeseok", 100:"Taeho"} #key는 string형태로도 할당 가능
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet["C-20"]="Seho"
cabinet[3]="Jongkook"
print(cabinet)

del cabinet[3]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)