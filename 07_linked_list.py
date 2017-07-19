class Node:
    # 생성자 함수
    def __init__(self, data):
        self.data = data
        self.next = None

    # 소멸자 함수
    def __del__(self):
        print('data of {} is deleted'.format(self.data))


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.before = None
        self.current = None

        self.num_data = 0
        # 인덱스 생성가능
        # self.idx = 0

    def empty(self):
        if self.num_data == 0:
            return True
        else:
            return False

    def size(self):
        return self.num_data

    def append(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.num_data += 1

    def traverse(self, mode='next'):
        if self.empty():
            return None
        if mode == 'first':
            self.before = self.head
            self.current = self.head
        # mode = 'next'
        else:
            if self.current.next == None:
            # if self.current == self.tail:
                return None
            self.before = self.current
            self.current = self.current.next

        return self.current.data

    def remove(self):
        # 레퍼런스 카운트를 0으로 만들어서 삭제

        # 3. 마지막 데이터를 삭제할때(tail, current가 삭제할 노드를 가리킬때)
        ret_data = self.current.data
        # 1. 1개만 남은 데이터를 삭제할때(before, current, head, tail이 남은 노드를 가리킬때)
        if self.size() == 1:
            self.head = None
            self.tail = None
            self.before = None
            self.current = None
        # 2. 첫번째 데이터를 삭제할때(head, current, before가 삭제할 노드를 가리킬때)
        # "is" 로 비교하면 주소값까지 같은지 비교
        elif self.current is self.head:
            self.head = self.head.next
            self.before = self.before.next
            self.current = self.current.next
        else:
            # 3. 마지막 데이터를 삭제할때(tail, current가 삭제할 노드를 가리킬때)
            if self.current is self.tail:
                self.tail = self.before
            self.before.next = self.current.next
            self.current = self.before
        self.num_data -= 1
        return ret_data


def show_list(slist):
    # 일단 first모드로 traverse 호출하여 data 존재 확인(데이터가 없으면 None)
    data = slist.traverse('first')
    # data가 있다면
    if data:
        print(data, end='   ')
        # 'next'모드로 traverse 호출
        data = slist.traverse()
        # None을 반환할때까지 순회
        while data:
            print(data, end='   ')
            data = slist.traverse()
    else:
        print("There is no data.")

if __name__ == "__main__":
    slist = LinkedList()
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")
    # 데이터 추가
    slist.append(2)
    slist.append(3)
    slist.append(1)
    slist.append(5)
    slist.append(2)
    slist.append(10)
    slist.append(7)
    slist.append(2)

    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")
    # 순회하며 2를 삭제
    data = slist.traverse('first')
    while data:
        if data == 2:
            slist.remove()
        data = slist.traverse()

    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")

    slist.append(3)

    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")
