# 경찰이 있고
# 총이 있는 경찰
# 총이 없는 경찰
# 총은 이름(멤버)과 발사(매서드)가 있어야 함

# 객체 합성: has-a 상태를 구현한 것 (상속하지 않음)
class Gun:
    def __init__(self, name):
        self.name = name

    def shoot(self):
        print("bbang")


class Policeman:
    def __init__(self):
        self.gun = None

    def set_gun(self, gun):
        self.gun = gun


# is-a (상속한다)
# laptop IS A computer

# has-a
# A policeman HAS A gun
