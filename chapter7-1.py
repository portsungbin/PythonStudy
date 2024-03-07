# # @@@@@@@@@@ 다양한 출력포맷 @@@@@@@@@@@@@@
# print("{0: >10}".format(500))
# #양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# #3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000))
# #3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(10000000))
# print("{0:+,}".format(-10000000))

# print("{0:^<+30,}".format(1000000000))
# print("{0:f}".format(5/3))
# #소수점 특정 자리수
# print("{0:.2f}".format(5/3)) #소수점 3째자리에서 반올림

# #@@@@@@@@@ 파일입출력 @@@@@@@@@@@@@@
# score = open("score.txt", "w",encoding="utf8")
# print("수학 : 0", file = score)
# print("영어 : 50", file = score)
# print("국어 : 80", file = score)
# score.close()

# score = open("score.txt", "a",encoding="utf8")
# score.write("과학 : 70")
# score.write("\n코딩 : 100 7-1")
# score.close()

# score = open("score.txt", "r",encoding="utf8")
# print(score.read())
# score.close()

# score = open("score.txt", "r",encoding="utf8")
# print(score.readline(), end = "") # readline = 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score.readline(), end = "")
# print(score.readline(), end = "")
# print(score.readline(), end = "")
# print(score.readline(), end = "")

#@@@@@@@@@@@ pickle @@@@@@@@@@@@@@
import pickle
profile = open("profile", "wb") #b는 피클을 사용하기 위해서 써줘야함

#@@@@@@@@@@@ with @@@@@@@@@@@@@@@@
#with open("score.txt", "r",encoding="utf8") as @@@@@   #with를 써서 close없이 간단하게 가능
    #score@@@@@.write("!!!!!!!!!!!")