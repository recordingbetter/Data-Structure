class Stack(list):
    push = list.append
    # 위 코드와 같다.
    # def push(self, data):
    #     super().append(data)

    # pop은 기존 list.pop 사용. 인자가 없으면 마지막 데이터를 삭제하고 반환

    def empty(self):
        # 데이터가 비어있는지 확인
        if not self:
            return True
        else:
            return False

    def peek(self):
        # 리스트의 마지막 데이터 반환
        return self[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s)

    while not s.empty():
        data = s.pop()
        print(data, end='   ')


