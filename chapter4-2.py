#튜플 (변경되지 않는 목록을 사용할때)

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 값을 추가하거나 변경은 불가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)



#집합(set)
#중복 안됨, 순서 없음
my = {1,2,3,3,3}
print(my)

java = {"유재석", "김태호", "양세형"}
python = set({"유재석", "박명수"})

#교집합(자바와 파이썬 모두 할수있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (자바도 할수있거나 파이썬을 할수있는 개발자) 순서는 보장되지 않음
print(java | python)
print(java.union(python))

# 차집합 (자바는 할수있지만 파이썬은 할줄모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할줄 아는사람이 늘어남
python.add("김태호")
print(python)

#java를 잊어버렸음
java.remove("김태호")
print(java)
