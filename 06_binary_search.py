def binary_search(data, target):
    """
    데이터가 정렬된 상태로 전달되어야 합니다.
    :param data: sorted list
    :param target: 찾는 숫자
    :return: 찾는 숫자의 인덱스
    """
    start = 0
    end = len(data) - 1
    count = 0
    while start <= end:

        mid = (start + end) // 2
        # target 과 mid 값이 같을 경우
        if target == data[mid]:
            count += 1
            return mid, count
        # target 이 중간값보다 작을 경우
        elif target < data[mid]:
            count += 1
            # end를 중간값 바로 전으로 이동
            end = mid - 1
        # target 이 중간값보다 작을 경우
        else:
            count += 1
            # start 를 중간값 다음으로 이동
            start = mid + 1
    # while 을 빠져나가는 경우는 end 와 start 가 교차되었을때
    return None


if __name__ == '__main__':
    li = [i for i in range(100)]
    target = 96
    idx = binary_search(li, target)
    if idx:
        print(li[idx[0]])
        print("{}번만에 찾았습니다.".format(idx[1]))
    else:
        print("There's no data")
