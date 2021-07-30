def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("sungwon", 25, "Java", "C", "C++", "C#", "Python")
profile("Sungwon", 26, "Kotlin", "Swift", "","","")

# (*language) 가변인자로 받는다
def profile2(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile2("sungwon", 25, "Python","Python","Python","Python","Python","Python")