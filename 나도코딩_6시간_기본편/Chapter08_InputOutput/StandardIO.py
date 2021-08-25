import sys
print("Python", file=sys.stdout)
print("Java", file=sys.stderr)

scores={"수학":0, "영어":50}
for subject, score in scores.items():
    #print(subject, score)의 정렬을 실행 ljust/rjust 사용
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) #zfill 남은 공간만큼 0으로 채움

answer=input("input : ")
print(answer)
print(type(answer))
#str 타입으로 저장

answer=10
print(answer)
print(type(answer))
#int 타입으로 저장