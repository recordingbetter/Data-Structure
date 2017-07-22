from binary_tree import *


class BinarySearchTree(BinaryTree):
    def insert(self, data):
        new_node = self.make_node()
        self.set_node_data(new_node, data)

        cur = self.get_root()
        if not cur:
            self.set_root(new_node)
            return

        while True:
            if data < self.get_node_data(cur):
                # left에 노드가 있으면
                if self.get_left_sub_tree(cur):
                    # cur를 이동
                    cur = self.get_left_sub_tree(cur)
                else:
                    # left에 노드가 없으면 그자리에 new_node를 넣고 종료
                    self.make_left_sub_tree(cur, new_node)
                    break
            else:
                if self.get_right_sub_tree(cur):
                    cur = self.get_right_sub_tree(cur)
                else:
                    self.make_right_sub_tree(cur, new_node)
                    break

    def search(self, target):
        cur = self.get_root()
        while cur is not None:
            if target == self.get_node_data(cur):
                return cur
            elif target < self.get_node_data(cur):
                cur = self.get_left_sub_tree(cur)
            else:
                cur = self.get_right_sub_tree(cur)
        return cur

    # def remove_left_sub_tree(self, cur):
    #     del_node = self.get_left_sub_tree(cur)
    #     self.make_left_sub_tree(cur, None)
    #     return del_node
    #
    # def remove_right_sub_tree(self, cur):
    #     del_node = self.get_right_sub_tree(cur)
    #     self.make_right_sub_tree(cur, None)
    #     return del_node

    def remove_leaf(self, parent, del_node):
        # 루트노드를 지울때
        if del_node == self.get_root():
            self.get_root(None)
            return del_node
        # 일반적인 경우
        if self.get_left_sub_tree(parent) == del_node:
            # self.remove_left_sub_tree(parent)
            self.make_left_sub_tree(parent, None)
        else:
            # self.remove_right_sub_tree(parent)
            self.make_right_sub_tree(parent, None)
        return del_node

    def remove_one_child(self, parent, del_node):
        # 지우려는 노드의 자식이 1개인 경우
        # 삭제할 노드가 root일 경우, root노드를 다음노드로 이동
        # parent가 가리키는 것은 스택프레임이 사라지면서 자동으로 사라짐
        if del_node == self.get_root():
            if self.get_left_sub_tree(del_node):
                self.set_root(self.get_left_sub_tree(del_node))
            else:
                self.set_root(self.get_right_sub_tree(del_node))
            return del_node

        # 삭제하려는 노드가 root가 아닐경우
        del_child = None
        # 지우려는 노드의 왼쪽에 자식이 있다면
        if self.get_left_sub_tree(del_node):
            del_child = self.get_left_sub_tree(del_node)
        else:
            del_child = self.get_right_sub_tree(del_node)
        # 지우려는 노드가 parent의 왼쪽에 있었을때
        if self.get_left_sub_tree(parent) == del_node:
            self.make_left_sub_tree(parent, del_child)
        # 지우려는 노드가 parent의 오른쪽에 있었을때
        else:
            self.make_right_sub_tree(parent, del_child)

    def remove_two_children(self, del_node):
        # root에 대한 예외처리가 필요없음
        # 지우려는 노드와 값을 바꿔서처리 (왼쪽으로1번, 이후에는계속오른쪽으로 이동하며비교 -> 트리에서 지우려는 노드보다 다음으로 큰값을 찾는다)
        # 왼쪽으로 1번이동
        rep_parent = del_node
        replace = self.get_left_sub_tree(del_node)
        # 오른쪽으로 이동하며 대체노드 찾음(오른쪽 자식이 더이상없을때까지)
        while self.get_right_sub_tree(replace):
            rep_parent = replace
            replace = self.get_right_sub_tree(replace)
        # 대체노드를 찾으면 값을 교환(이 코드는 c 방식)
        temp_data = self.get_node_data(replace)
        self.set_node_data(replace, self.get_node_data(del_node))
        self.set_node_data(del_node, temp_data)
        # 부모의 왼쪽에 붙어있었다면 !!!
        if self.get_left_sub_tree(rep_parent) == replace:
            #
            self.make_left_sub_tree(rep_parent, self.get_left_sub_tree(replace))
        # 부모의 오른쪽에 붙어있었다면
        else:
            self.make_right_sub_tree(rep_parent, self.get_left_sub_tree(replace))
        return replace

    def remove(self, target):
        del_parent = self.get_root()
        del_node = self.get_root()
        while True:
            if del_node is None:
                return None
            # 지우려는 노드를 찾았을때
            if target == self.get_node_data(del_node):
                break
            # 지우려는 노드가 현재 노드보다 작을 경우
            elif target < self.get_node_data(del_node):
                # 하나씩 이동
                del_parent = del_node
                del_node = self.get_left_sub_tree(del_node)
            # 지우려는 노드가 현재 노드보다 클 경우
            else:
                del_parent = del_node
                del_node = self.get_right_sub_tree(del_node)
        # target의 자식에 따라 remove 종류를 다르게 적용
        if self.get_left_sub_tree(del_node) is None and self.get_right_sub_tree(del_node) is None:
            return self.remove_leaf(del_parent, del_node)
        # 지우려는 노드의 자식 노드가 1개일때
        elif self.get_left_sub_tree(del_node) is None or self.get_right_sub_tree(del_node) is None:
            return self.remove_one_child(del_parent, del_node)
        # 지우려는 노드의 자식노드가 2개일때
        else:
            return self.remove_two_children(del_node)


if __name__ == "__main__":
    bst = BinarySearchTree()

    # 트리노드생성
    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f = lambda x: print(x, end='    ')
    # 전위순회
    bst.preorder_traverse(bst.get_root(), f)
    print('\n')

    # remove
    # bst.remove(9) # 말단노드 삭제
    # bst.remove(8) # 자식이 1개인 노드 삭제
    bst.remove(6) # 자식이 2개인 노드 삭제
    bst.preorder_traverse(bst.get_root(), f)
    print('\n')

