# Поиск наибольшего элемента, используя рекурсию. [O(n)]

def find_max_element(list_two):
    if len(list_two) == 0:
        return None
    if len(list_two) == 1:
        return list_two[0]
    else:
        sub_max = find_max_element(list_two[1:])
        return list_two[0] if list_two[0] > sub_max else sub_max
