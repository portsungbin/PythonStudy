#@@@@@@@@ 함수호출(기본값, 키워드값) @@@@@@@@@@@@@@@
# def pro(name, age = 17, main = "파이썬"):
#     print("이름 :  {0}\t나이 :  {1}\t주 사용 언어 {2}".format(name, age, main))

# pro("유재석")

# def pro(name, age, main):
#     print(name, age, main)

# pro(name="유재석", main = "파이썬", age=20)



#@@@@@@@@@@ 가변인자 @@@@@@@@@@@@@@
# def pro(name, age, lg1, lg2, lg3, lg4, lg5):
#     print("이름 :  {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lg1,lg2,lg3,lg4,lg5)

def pro(name, age, *lg):  # *로 매개변수를 활용 
    print("이름 :  {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in lg:
        print(lang, end = " ")
    print()

pro("우재석", 20, "파이썬","자바","C", "자바스크립트", "C++","c#")
pro("김태호", 20, "kotlin", "swift")