class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        dummy = Node("dummy")

        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data += 1

    def first(self):
        if not self.num_of_data:
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    def next(self):
        if not self.current.next:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def delete(self):
        ret_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before
        self.num_of_data -= 1

        return ret_data

    def size(self):
        return self.num_of_data

    def show_list(self):
        data = self.first()

        if data:
            print(data, end='  ')
            data = self.next()
            while data:
                print(data, end='  ')
                data = self.next()
        else:
            print("there is no data")


if __name__ == "__main__":
    d_list = linked_list()
    print("데이터의 개수 : {}".format(d_list.size()))
    d_list.show_list()
    print("\n")

    d_list.append(2)
    d_list.append(3)
    d_list.append(1)
    d_list.append(5)
    d_list.append(2)
    d_list.append(10)
    d_list.append(7)
    d_list.append(2)

    print("데이터의 개수 : {}".format(d_list.size()))
    d_list.show_list()
    print("\n")

    data = d_list.first()
    if data == 2:
        d_list.delete()
        print("deleted", end='  ')
    elif data:
        print(data, end='  ')

    while True:
        data = d_list.next()
        if data == 2:
            d_list.delete()
            print("deleted", end='  ')
        elif data:
            print(data, end='  ')
        else:
            break



