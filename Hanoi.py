def hanoi(num, _from, _by, _to):
    # 탈출조건
    if num == 1:
        print("{}에서 {}로 {}번째 원반 이동".format(_from, _to, num))
        return
    hanoi(num - 1, _from, _to, _by)
    print("{}에서 {}로 {}번째 원반 이동".format(_from, _to, num))
    hanoi(num - 1, _by, _from, _to)


if __name__ == "__main__":
    while 1:
        numOfTray = int(input("원반의 갯수를 입력하세요(종료:0) :"))
        if numOfTray == 0:
            break
        hanoi(numOfTray, 'A', 'B', 'C')
