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


class unit:
    def __init__(self, name, hp, damage): #__init__ 함수와 동일하게 self 를 제외한 값을 객체(마린, 탱크)에 넣어야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0}, 공격력{1}".format(self.hp, self.damage))

marin1 = unit("마린", 40, 5)
marin2 = unit("마린", 40, 5)
tank1 = unit("탱크", 350, 35)
    