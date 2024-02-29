#@@@@@@@@@@@@@@ 표준 입출력 @@@@@@@@@@@@@@@@@
print("파이썬","자바","자바스크립트", sep=" vs ", end = "?") #콤마 사이사이에 sep=""에 들어간걸 넣어줌
print("무엇이 더 재밌을까요???") # end를 통해 줄바꿈을 하지 않고 문자를 넣고 한줄로 출력

import sys
print("파이썬","자바","자바스크립트", file=sys.stdout) #표준 출력어
print("파이썬","자바","자바스크립트", file=sys.stderr) #표준 에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":") # .ljist(8) = 왼쪽정렬 8칸 확보 .rjust(4) = 오른쪽정렬 4칸 확보


#은행 대기순번표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # .zfill(3) = 3개의 공간을 확보후 값을 집어넣는데 값이 없는부분은 0으로 채움


answer = input("아무 값이나 입력하세요 : ") #사용자입력을 통해서 값을 받게 된다면 문자열 형태로 저장이 됨
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")