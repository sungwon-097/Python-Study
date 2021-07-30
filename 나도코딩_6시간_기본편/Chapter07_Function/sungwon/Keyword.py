#함수 사용 시 키워드의 순서가 달라도 정상동작함

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="성원", main_lang="파이썬", age=20)
profile(main_lang="자바", age=20, name="성원")