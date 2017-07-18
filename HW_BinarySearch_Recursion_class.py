def binary_search(target, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(target, start, end, data)


if __name__ == "__main__":
    data = [i ** 2 for i in range(1, 11)]

    target = 4
    start = 0
    end = len(data) - 1
    idx = binary_search(target, start, end, data)
    if idx:
        print(data[idx])
    else:
        print("There's no data.")
