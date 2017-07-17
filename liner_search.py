def liner_search(data, target):
    for idx in range(len(data)):
        if data[idx] == target:
            return idx
        return None


if __name__ == "__main__":
    data = [i for i in range(10)]
    target = 4
    idx = liner_search(data, target)

    if idx is None:
        print("{}이 존재하지 않습니다.".format(target))
    else:
        print("찾는 데이터의 인덱스는 {}이고 데이터는 {}입니다.".format(idx, data[idx]))
