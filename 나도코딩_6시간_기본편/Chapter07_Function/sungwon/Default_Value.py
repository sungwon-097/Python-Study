#함수 선언 시 기본값을 설정 가능

def profile(name, age=17, main_lang="Python"):
    print("Name : {0}\t Age : {1}\tMain Language : {2}"\
        .format(name, age, main_lang))

profile("sungwon")
profile("Sungwon")