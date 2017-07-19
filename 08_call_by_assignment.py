class Base:
    def __init__(self, a):
        self.a = a

    def set_a(self, new_a):
        self.a = new_a


def func(b, data):
    # b.set_a(data)
    b = Base(data)

if __name__ == "__main__":
    b = Base(4)
    print(b.a)
    func(b, 10)
    print(b.a)

