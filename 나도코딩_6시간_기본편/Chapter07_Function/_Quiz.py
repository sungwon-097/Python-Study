'''표준 체중을 구하는 프로그램 작성

남성 : 키(미터)^2*22
여성 : 키(미터)^2*21

'''

def std_weight(height, gender):
    if(gender=="male"):
        return 