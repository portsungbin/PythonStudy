sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("월 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터)" + jumin[-7:])

python = "Python is Amazing"
print(python.lower()) #소문자
print(python.upper()) #대문자
print(python[0].isupper()) #0번째 문자가 대문자인가?
print(len(python)) #문자 길이
print(python.replace("Python", "Java")) #파이썬을 자바로 변경

index = python.index("n") #첫번째 나오는 n의 위치
print(index)
index = python.index("n", index + 1) #두번째 나오는 n의 위치
print(index)

print(python.find("Java")) #에러가 나지 않고 없으면 -1로 나타냄
#print(python.index("Java")) #Java가 없기 때문에 에러를 내버리고 프로그램을 끝내버림

print(python.count("n")) #n이 몇개인가

print("a" + "b")
print("a", "b")
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple 은 %c로 시작해요" % "A")

print("나는 %s살입니다." % 20) # %s 는 다 사용가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강")) # "파란"이 0번쨰 "빨강"이 1번째

print("나는 {age}살이며 {color}색을 좋아해요.".format(age = 20, color = "빨강"))

age = 20
color = "빨강"
print(f"나는 {age}살이며 {color}색을 좋아해요.") # 앞에 f를 붙이면 변수값 가져가서 쓰기 가능


#탈출문자
print("백문이 불여일견 \n백견이 불여일타") # \n = 줄바꿈
print('저는 "나도코딩"입니다')# 저는"나도코딩"입니다 만들기
print("저는 \"나도코딩\"입니다") #역슬러시
# \\ : 문장 내에서 \
print("C:\\Users\\ㅅㅂ\\OneDrive\\바탕 화면\\pythonstudy\\PythonStudy>") # 2개씩 적어야 나옴

print("red apple \rpine") #\r (pine)커서를 맨앞으로 이동
print("red\bapple") # \b : 백스페이스(한글자 삭제)
print("red\tapple") # \t : 키보드 탭 누른효과
