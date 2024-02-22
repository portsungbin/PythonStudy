#사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#print(cabinet(5)) #키가 없기때문에 오류발생시키고 프로그램을 끝냄
#print("hi")
print(cabinet.get(5)) # 값이 없다면 None이라는 값을 출력후 프로그램 진행
print(cabinet.get(5, "사용가능"))
print("hi")
print(3 in cabinet) #키값이 있다면Ture
print(5 in cabinet) #키값이 없다면False

cabinet = {"A":"유재석", "B":"김태호"} #문자키도 가능
print(cabinet["A"])
print(cabinet["B"])

#새 손님
print(cabinet)
cabinet["A"] = "김종국" #유재석이 빠지고 김종국이 들어감(업데이트)
cabinet["C"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A"]
print(cabinet)

#키들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)