def quick_sort(data, start, end):
    """
    quick sort
    :param data: list
    :param start: 시작 데이터 인덱스
    :param end: 마지막 데이터 인덱스
    :return: sorted list
    """
    # 탈출조건 : start와 end가 교차되었을 경우
    if start > end:
        return
    left = start
    right = end
    # pivot은 데이터 값
    pivot = data[(start + end) // 2]
    print("p")
    # left와 right가 교차되면 while을 빠져나감
    while left <= right:
        # left가 pivot보다 작을경우 오른쪽으로 이동, 크면 while을 빠져나감
        while data[left] < pivot:
            left += 1
        # right가 pivot보다 클경우 왼쪽으로 이동, 작으면 while을 빠져나감
        while data[right] > pivot:
            right -= 1

        # left와 right가 교차되지 않았는지 확인
        # 교차되지 않았다면
        if left <= right:
            # left와 right의 데이터 교환
            data[left], data[right] = data[right], data[left]
            # 한칸씩 이동
            left += 1
            right -= 1

    quick_sort(data, start, right)
    quick_sort(data, left, end)


if __name__ == "__main__":
    data = [7, 3, 5, 2, 6, 1, 4, 3, 2, 7]
    quick_sort(data, 0, len(data) - 1)
    print(data)
