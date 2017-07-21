class Stack:
    push = list.append
    pop = list.pop

    def empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[-1]


class Calculator:
    def __init__(self):
        self.org_exp = None
        self.postfix_exp = None
        self.result = None

    def set_org_exp(self, org_exp):
        self.org_exp = org_exp.replace(' ', '')
        self.postfix_exp = None
        self.result = None

    def get_org_exp(self):
        # 접근자
        return self.org_exp