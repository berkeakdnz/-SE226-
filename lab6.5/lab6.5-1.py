list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


def common_elements(list1, list2):
    return [elem for elem in list1 if elem in list2]


common = common_elements(list1, list2)
print(common)
