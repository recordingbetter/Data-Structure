def binary_search_re(start, end, target):
    lst = [i for i in range(start, end + 1)]
    mid = len(lst) // 2
    num = lst[mid]
    if start > end:
        return 1
    elif target == num:
        return num
    elif target < num:
        return binary_search_re(start, lst[mid - 1], target)
    else:
        return binary_search_re(lst[mid + 1], end, target)


if __name__ == '__main__':
    start = 1
    end = 11
    target = 2
    result = binary_search_re(start, end, target)
    if result:
        print(result)
    else:
        print("There's no data.")
