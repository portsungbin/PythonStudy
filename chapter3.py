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