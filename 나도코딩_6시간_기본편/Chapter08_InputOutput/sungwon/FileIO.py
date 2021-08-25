score_file=open("score.txt", "w", encoding="utf8") #w는 만들기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close #항상 닫아줌


score_file=open("score.txt", "a", encoding="utf8") #a는 덮어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")

score_file=open("score.txt", "r", encoding="utf8") #r은 읽기
print(score_file.read())
score_file.close()

score_file=open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄 별로 읽기 동작, 한 줄을 읽고 커서는 다음 줄로
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

#줄 수를 모를 때
score_file=open("score.txt", "r", encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file=open("score.txt", "r", encoding="utf8")
lines=score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

#세 가지 모두 같은 방법