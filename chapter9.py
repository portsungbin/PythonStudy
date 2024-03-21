# #@@@@@@@@@@@@@@ 예외 처리 @@@@@@@@@@@@@@
# try: #잘 실행되다가 ValueError에러가 뜬다면 밑에로 실행됨
#     print("나누기 전용 계산기 입니다")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError: #
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다")
#     print(err)



#@@@@@@@@@@@@ 에러 발생시키기, 사용자 정의 예외처리, finally @@@@@@@@@@@@@@@@@
#에러로 인해 없는파일을 연다던지 문제를 발생했을때 강제종료를 막음으로서 완성도를 높임
class bignumberError(Exception):
    def __init__(self, msg): #클래스 안의 필수존재
        self.msg = msg

    def __repr__(self): 
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise bignumberError("입력값 : {0} : {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError as err2: #내장에러
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
    print(err2)
except bignumberError as err:
    print("에러가 발생하였습니다 한자리 숫자만 입력하세요.")
    print(err)
finally: #오류가 뜨던 출력이 되던 무조건 출력됨
    print("계산기를 이용해 주셔서 감사합니다.")