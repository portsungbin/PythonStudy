#@@@@@@@@@@ 함수 @@@@@@@@@@@@@
# def open(): #함수쓰는방법
#     print("새로운 계좌가 생성되었습니다")

# open() #함수 호출방법

def deposit(balance, money): #입금 balance = 잔액 money = 현재돈
    print("입금이 완료되었습니다 잔액은 {0} 원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면 출금가능
        print("출금이 완료 되었습니다 잔액은 {0}원 입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다 잔액은 {0}원 입니다".format(balance))
        return balance
    
def night(balance, money):
    commission = 100 #야간수수료 100원
    if balance <= money:
        print("출금이 완료되지 않았습니다 잔액은 {0}원 입니다".format(balance))
        if balance - money - commission < 0:
            return commission, money
    
    
    return commission, balance - money - commission
    
balance = 0 #잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = night(balance, 500)
print("수수료는 {0}원 이며 잔액은 {1}원 입니다".format(commission, balance))