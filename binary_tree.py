class TreeNode:
    def __init__(self):
        self._data = None
        self.left = None
        self.right = None

    # 소멸자 - 데이터를 메모리에서 삭제하기 전에 호출된다.
    def __del__(self):
        print("TreeNode of {} is deleted.".format(self.data))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, r):
        self.root = r

    def make_node(self):
        # 이진트리의 모든 기능을 구현하는 클래스라 추가함.
        # 노드의 생성을 위임함. (캡슐레이션)
        new_node = TreeNode()
        return new_node

    def get_node_data(self, cur):
        return cur.data

    def set_node_data(self, cur, data):
        cur.data = data

    def get_left_sub_tree(self, cur):
        return cur.left

    def get_right_sub_tree(self, cur):
        return cur.right

    def make_left_sub_tree(self, cur, left):
        cur.left = left

    def make_right_sub_tree(self, cur, right):
        cur.right = right

    def preorder_traverse(self, cur, func):
        # 전위순회
        if cur == None:
            return
        func(cur.data)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def inorder_traverse(self, cur, func):
        # 중위순회
        if not cur:
            return
        self.inorder_traverse(cur.left, func)
        func(cur.data)
        self.inorder_traverse(cur.right, func)

    def postorder_traverse(self, cur, func):
        # 후위순회
        if not cur:
            return
        self.postorder_traverse(cur.left, func)
        self.postorder_traverse(cur.right, func)
        func(cur.data)


if __name__ == "__main__":
    bt = BinaryTree()
    # 노드를 생성하는 것을 함수에 위임함. 7개의 노드 생성
    n1 = bt.make_node()
    bt.set_node_data(n1, 'A')

    n2 = bt.make_node()
    bt.set_node_data(n2, 'B')

    n3 = bt.make_node()
    bt.set_node_data(n3, 'C')

    n4 = bt.make_node()
    bt.set_node_data(n4, 'D')

    n5 = bt.make_node()
    bt.set_node_data(n5, 'E')

    n6 = bt.make_node()
    bt.set_node_data(n6, 'F')

    n7 = bt.make_node()
    bt.set_node_data(n7, 'G')

    n8 = bt.make_node()
    bt.set_node_data(n8, 'H')

    # 트리의 루트 설정
    bt.set_root(n1)
    # 1번 노드에 2, 3번을 자식으로 붙임
    bt.make_left_sub_tree(n1, n2)
    bt.make_right_sub_tree(n1, n3)
    # 2번 노드에 4, 5번을 자식으로 붙임
    bt.make_left_sub_tree(n2, n4)
    bt.make_right_sub_tree(n2, n5)
    # 3번 노드에 6, 7번을 자식으로 붙임
    bt.make_left_sub_tree(n3, n6)
    bt.make_right_sub_tree(n3, n7)

    # 1번 노드에 8번 노드를 자식으로 붙임
    bt.make_right_sub_tree(n1, n8)
    # 8번 노드에 3번 노드를 자식으로 붙임
    bt.make_right_sub_tree(n8, n3)

    # 3, 8 노드 삭제를 위해 1 - 6 노드 연결
    bt.make_right_sub_tree(n1, n6)
    # 6번 노드의 자식으로 7번 노드를 연결
    bt.make_right_sub_tree(n6, n7)
    # 3, 8번 노드 삭제
    del n3, n8

    # 노드값을 출력(람다는 호출되지않으면 사라짐)
    f = lambda x: print(x, end='    ')

    # 전위순회
    bt.preorder_traverse(bt.get_root(), f)
    print('\n')
    # 중위순회
    bt.inorder_traverse(bt.get_root(), f)
    print('\n')
    # 후위순회
    bt.postorder_traverse(bt.get_root(), f)
    print('\n')





