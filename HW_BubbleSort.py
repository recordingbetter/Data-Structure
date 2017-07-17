def bubble(lst):
    lst_len = len(lst)
    for i in range(lst_len):
        for j in range(0, lst_len - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(lst)

lst = [4, 7, 9, 3, 4, 6, 2, 7, 1]
print(bubble(lst))


