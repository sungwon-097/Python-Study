'''
당신은 택시 기사이다
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성.

조건1: 승객별 운행 소요 시간은 5분~10분 사이의 난수
조건2: 소요시간 5분~15분 사이의 승객만 매칭해야 한다.
'''

from random import *
customer=0
check_time=True
current_time=0
total_customer=0
while(customer<50):
    customer+=1
    current_time=randint(5,50)
    check_time=(5<=current_time<=15)
    check='O'
    if check_time==False:
        check=' '
    else:
        total_customer+=1
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, customer, current_time))
print("총 탑승 승객 : " + str(total_customer))
