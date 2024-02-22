#리스트 []
subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

#조세호가 몇번째 칸에 타있는가
print(subway.index("조세호"))

#하하가 다음 정류장에서 탐
subway.append("하하")
print(subway)

#정현돈을 유재석 조세호 사이에 태움
subway.insert(1, "정현돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명인가
subway.append("유재석")
print(subway)
print(subway.count("유재석")) #같은값이 몇번나오는가

#정렬도 가능
num = [5,2,4,3,1]
num.sort()
print(num)

#순서 뒤집기
num.reverse()
print(num)

#모두 지우기
num.clear()
print(num)

#다양한 자료형 함께 사용
mix = ["조세호", 20, True]
print(mix)

#리스트 확장
num = [5,2,4,3,1]
num.extend(mix)
print(num)



