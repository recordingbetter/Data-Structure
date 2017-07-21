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

    def remove_left_sub_tree(self, cur):
        del_node = self.get_left_sub_tree(cur)
        self.make_left_sub_tree(cur, None)
        return del_node

    def remove_right_sub_tree(self, cur):
        del_node = self.get_right_sub_tree(cur)
        self.make_right_sub_tree(cur, None)
        return del_node

    def remove_leaf(self, parent, del_node):
        # 루트노드를 지울때
        if del_node == self.get_root():
            self.get_root(None)
            return del_node
        # 일반적인 경우
        if self.get_left_sub_tree(parent) == del_node:
            self.remove_left_sub_tree(parent)
        else:
            self.remove_right_sub_tree(parent)
        return del_node

    def remove_one_child(self, parent, del_node):
        pass

    def remove_two_children(self, del_node):
        pass

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
        if self.get_left_sub_tree(del_node) is None and self.get_right_sub_tree(del_node) is None:
            return self.remove_leaf(del_parent, del_node)
        elif self.get_left_sub_tree(del_node) is None or self.get_right_sub_tree(del_node) is None:
            return self.remove_one_child(del_parent, del_node)
        else:
            return self.remove_two_children(del_parent, del_node)

