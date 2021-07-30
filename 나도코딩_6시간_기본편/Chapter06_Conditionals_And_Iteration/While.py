customer="토르"
index=5
while index>=1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
    index-=1
    if index==0:
        print("커피가 폐기되었습니다.")

#무한루프
customer ="아이언맨"
index=1
while True:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
    index+=1

print