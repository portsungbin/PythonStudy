# @@@@@@@@@@@ 모듈 @@@@@@@@@@@@@ 
# 필요한것들로 부품처럼 잘 만드는것

#일반가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

#조조 할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

#군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인가격은{1}원 입니다.".format(people, people * 4000))
