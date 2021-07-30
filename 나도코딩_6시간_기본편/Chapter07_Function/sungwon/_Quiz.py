'''표준 체중을 구하는 프로그램 작성

남성 : 키(미터)^2*22
여성 : 키(미터)^2*21

'''

def std_weight(height, gender):
    if(gender=="남자"):
        return height*height*22
    else:
        return height*height*21

height=1.75
gender="남자"
print(f"키 {height*100}cm {gender} 표준 체중은 {round(std_weight(height, gender), 2)}입니다.")