#@@@@@@@@@@ 조건문 @@@@@@@@@@@@@@@
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지 마세요")



#@@@@@@@@@@@@ 반복문for @@@@@@@@@@@@@@@
# for waiting in range(1, 6):  #1,2,3,4,5
#     print("대기번호 : {0}".format(waiting))

# st = ["아이언맨", "토르", "그루트"]
# for cu in st:
#     print("{0}, 커피가 준비되었습니다".format(cu))



#@@@@@@@@@@ 반복문while @@@@@@@@@@@@@
# cust = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 손님의 커피가 준비되었습니다 {1}번 남았어요".format(cust, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# cust = "토르"
# index = "UnKnown"
# while index != cust:
#     print("{0}, 커피가 준비되었습니다".format(cust))
#     index = input("이름이 어떻게 되세요? ")



#@@@@@@@@@ continue 와 break @@@@@@@@@@@
# absent = [2, 5] #결석
# nobook = [7] #책을 깜빡했음
# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue #계속해서 다음반복문을 진행
#     elif student in nobook:
#         print("오늘 수업 여기까지 {}학생 교무실로 와".format(student))
#         break #반복문을 진행하지 않고 바로끝냄
#     print("{0}, 책을 읽어봐".format(student))



#@@@@@@@@@@ 한줄 for문 @@@@@@@@@@@@@@@@
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

#학생 이름을 길이로 변환
# student = ["man", "thor", "groot"]
# student = [len(i) for i in student]
# print(student)

#학생이름을 대문자로 변환
# student = ["man", "thor", "groot"]
# student = [i.upper() for i in student]
# print(student)