#@@@@@@@@@@@@ 모듈 사용 @@@@@@@@@@@@@

# import chapter10ex
# chapter10ex.price(3)
# chapter10ex.price_morning(4)
# chapter10ex.price_soldier(5)

# import chapter10ex as mv  #as 는  chapter10ex 를 대신해서 쓸것을 정함
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from chapter10ex import *
# #from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

from chapter10ex import price, price_morning
price(5)
price_morning(6)
#price_soldier(7) 쓸수없음

from chapter10ex import price_soldier as price
price(5)
