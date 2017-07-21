# 가정 : 입력된 수식을 1자리 수의 계산

from stack import Stack


class Calculator:
    def __init__(self):
        self.org_exp = None  # 중위표기법 (사용자 입력 수식)
        self.postfix_exp = None  # 후위표기법
        self.result = None

    def set_org_exp(self, org_exp):
        # 입력한 수식 정리하는 함수
        self.org_exp = org_exp.replace(' ', '')
        # 초기화 (이전 계산값이 남아있을수 있으므로)
        self.postfix_exp = None
        self.result = None

    def get_org_exp(self):
        return self.org_exp

    def get_weight(self, oprt):
        # 연산자 별로 가중치를 부여하는 함수
        if oprt == '*' or oprt == '/':
            return 9
        elif oprt == '+' or oprt == '-':
            return 7
        elif oprt == '(':
            return 5

    def convert_to_postfix(self):
        # 입력된 수식을 후위표기법으로 변환하는 함수
        # 리스트 초기화
        exp_list = []
        # stack 선언
        oprt_stack = Stack()
        # 입력된 수식을 한글자씩 순회
        for ch in self.get_org_exp():
            # ch가 숫자일때
            if ch.isdigit():
                # 리스트에 추가
                exp_list.append(ch)
            # 연산자일때
            else:
                # ( 이거나 스택이 비었을때
                if oprt_stack.empty() or ch == '(':
                    # stack에 쌓는다.
                    oprt_stack.push(ch)
                # ) 일때
                elif ch == ')':
                    # stack의 마지막 데이터를 지우면서 가지고 와서
                    op = oprt_stack.pop()
                    # op가 ( 이 아니라면
                    while op != '(':
                        # 리스트에 추가
                        exp_list.append(op)
                        # 다시 stack의 마지막 데이터를 지우면서 가지고 와서 ( 가 나올때까지 while
                        op = oprt_stack.pop()
                # +, -, *, / 일때
                # ch의 가중치가 stack에 있는 연산자의 가중치가 작거나 같을때
                elif self.get_weight(ch) > self.get_weight(oprt_stack.peek()):
                    oprt_stack.push(ch)
                else:
                    # ch의 가중치가 stack에 있는 연산자의 가중치가 작거나 같을때
                    # oprt_stack 가 비어있지않은지 먼저 확인하고 가중치 비교
                    while oprt_stack and self.get_weight(ch) <= self.get_weight(oprt_stack.peek()):
                        # 스택에서 삭제하면서 리스트에 추가
                        exp_list.append(oprt_stack.pop())
                    #
                    oprt_stack.push(ch)
        # 다 돌고나서 연산자가 남아있을 경우
        while oprt_stack:
            exp_list.append(oprt_stack.pop())
        self.postfix_exp = ''.join(exp_list)

    def get_postfix_exp(self):
        # 캐시 기법
        if not self.postfix_exp:
            self.convert_to_postfix()
        return self.postfix_exp

    # 필수는 아니지만 편의를 위해 만든 함수
    def calc_two_oprd(self, oprd1, oprd2, oprt):
        if oprt == '+':
            return oprd1 + oprd2
        elif oprt == '-':
            return oprd1 - oprd2
        elif oprt == '*':
            return oprd1 * oprd2
        elif oprt == '/':
            return oprd1 / oprd2

    def calculator(self):
        oprd_stack = Stack()
        # 접근자가 있으면 클래스외부에서 접근할땐 항상 그함수를 통해 접근해야함.
        for ch in self.get_postfix_exp():
            if ch.isdigit():
                oprd_stack.push(int(ch))
            else:
                oprd2 = oprd_stack.pop()
                oprd1 = oprd_stack.pop()
                oprd_stack.push(
                        self.calc_two_oprd(oprd1, oprd2, ch)
                )
        self.result = oprd_stack.pop()

    def get_result(self):
        if not self.result:
            self.calculator()
        return self.result


if __name__ == "__main__":
    calc = Calculator()
    while 1:
        exp = input("수식을 입력하세요.(종료:0):")
        if exp == '0':
            break

        calc.set_org_exp(exp)
        print(calc.get_postfix_exp())
        print('{exp} = {result}'.format(
                exp=calc.get_org_exp(),
                result=calc.get_result()
        ))
