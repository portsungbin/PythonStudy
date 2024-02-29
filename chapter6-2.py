# @@@@@@@@@@@ 지역변수 와 전역변수 @@@@@@@@@@@@@@@@@@

gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용 (전역변수)
    #gun = 20  #지역변수
    gun = gun - soldiers
    print("(함수 내) 남은 총 : {0}".format(gun))

def check(gun, soldiers):
    gun = gun - soldiers
    print("(함수 내) 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = check(gun, 2) #2명이 경계근무나감
print("남은 총 : {0}".format(gun))