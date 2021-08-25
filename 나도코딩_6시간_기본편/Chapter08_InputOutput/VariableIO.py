#빈 자리는 빈공간으로 두고 오른쪽 정렬을 하되 총 10자리 공간을 확보
print("{0: >10}".format(500))

#양수일 떈 + 음수일 땐 -표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽정렬하고 빈 칸을 _로 채움
print("{0:_<10}".format(500))

#세자리마다 콤마 찍어주기
print("{0:,}".format(50000000000000))
print("{0:+,}".format(50000000000000))

#세자리마다 콤마, 부호, 자리수 확보, 빈자리는 ^
print("{0:^>+30,}".format(50000000000000))
\
#소숫점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))