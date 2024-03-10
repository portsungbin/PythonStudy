#@@@@@@@@@@@@@@@@@ 클래스 @@@@@@@@@@@@@@@@@@@
# 마린 : 공격유닛, 공격 총을쏨
# name = "마린" #유닛의 이름
# hp = 40 #유닛의 체력
# damage = 5 #유닛의 공격력
# print("{0} 유닛이 생성되었습니다".format(name))
# print("체력 {0},  공격력 {1}\n".format(hp, damage))

# t_name = "탱크"
# t_hp = 150
# t_damage = 35
# print("{0} 유닛이 생성되었습니다".format(t_name))
# print("체력 {0},  공격력 {1}\n".format(t_hp, t_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(name,location, damage))

# attack(name,"1시", damage)
# attack(t_name, "1시", t_damage)


#@@@@@@@@@@@@ unit, 메소드 @@@@@@@@@@@@@@
# class unit: #일반 유닛
#     def __init__(self, name, hp, damage): #__init__ 함수와 동일하게 self 를 제외한 값을 객체(마린, 탱크)에 넣어야함
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력{0}, 공격력{1}".format(self.hp, self.damage))

# class attackunit: #공격 유닛
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack(self, location): #메소드
#         print("{0} : {1} 방향으로 적군을 공격합니다 [공격력 : {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage): #메소드
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #파이어뱃
# firebat = attackunit("파이어뱃", 50, 16)
# firebat.attack("5시")

# firebat.damaged(25)
# firebat.damaged(25)




#@@@@@@@@@@@@@ 상속 @@@@@@@@@@@@@@@@
from random import *
class unit: #일반 유닛
    def __init__(self, name, hp, speed): #__init__ 함수와 동일하게 self 를 제외한 값을 객체(마린, 탱크)에 넣어야함
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage): #메소드
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class attackunit(unit): #공격 유닛
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location): #메소드
        print("{0} : {1} 방향으로 적군을 공격합니다 [공격력 : {2}]".format(self.name, location, self.damage))

#마린
class marine(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 40, 1, 5)

        #스팀팩
    def stim(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다 (hp 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 못합니다".format(self.name))

class tank(attackunit):
    #시즈모드(이동불가)
    seize = False

    def __init__(self):
        attackunit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize(self):
        if tank.seize == False:
            return
        
        #현재 시즈모드가 아닐 때
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다".format(self.name))
            self.damage /= 2
            self.seize_mode = False


        #현재 시즈모드 일 때


#@@@@@@@@@@@@@ 다중 상속, 메소드 오버라이딩 @@@@@@@@@@@@@@@@@@
#드랍쉽 : 공중유닛, 수송기, 공격기능x
class flyable: #날수있는 기능을가진 클래스
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다 [속도 : {2}]".format(name, location, self.fly_speed))

#공중 공격 유닛 클래스
class flyattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, fly_speed):
        attackunit.__init__(self, name, hp, 0, damage) #지상 speed 0
        flyable.__init__(self, fly_speed)
    
    def move(self, location):
        self.fly(self.name, location)

#레이스
class wraith(flyattackunit):
    def __init__(self):
        flyattackunit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드로 설정합니다".format(self.name))
            self.clocked = True

def game_start():
    print("새로운 게임을 시작합니다")

def game_over():
    print("player : gg")
    print("player님이 게임에서 퇴장하였습니다")

#실제 게임 진행
game_start()

#마린 3
m1 = marine()
m2 = marine()
m3 = marine()

#탱크 = 2
t1 = tank()
t2 = tank()

#레이스 1
w1 = wraith()


#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
tank.seize = True
print("탱크 시즈모드 개발 완료되었습니다")

#공격 모드 준비
for unit in attack_units:
    if isinstance(unit, marine):
        unit.stim()
    elif isinstance(unit, tank):
        unit.set_seize()
    elif isinstance(unit, wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음

#게임 종료
game_over()


#건물
# class buildingunit(unit):
#     def __init__(self, name, hp, location):
#         #unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) #슈퍼를 쓸땐 괄호랑 self를 쓰지 않는다
#         self.location = location


# #서플라이 디폿 : 유닛8생성
# supply = buildingunit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("새로운게임시작")
# def game_over():
#     pass #그냥 넘어감
# game_start()
# game_over()




# marin1 = unit("마린", 40, 5)
# marin2 = unit("마린", 40, 5)
# tank1 = unit("탱크", 350, 35)


#@@@@@@@@@@@ 멤버변수 @@@@@@@@@@@@@@

# #레이스 :  공중유닛, 비행기, 클로킹
# wraith = unit("레이스", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith.name, wraith.damage))

# #마인드 컨트롤
# wraith1 = unit("빼앗은 레이스", 80, 5)
# wraith1.clocking = True

# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith1.name))