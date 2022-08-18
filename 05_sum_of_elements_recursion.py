# Сумма элементов, используя рекурсию. [O(n)]

def sum_of_elements(list_of_elem):
    if len(list_of_elem) == 1:
        return list_of_elem[0]
    else:
        return list_of_elem.pop(0) + sum_of_elements(list_of_elem)


def sum_of_elements_second_solution(list_of_elem):
    if len(list_of_elem) == 0:
        return 0
    else:
        return list_of_elem[0] + sum_of_elements_second_solution(list_of_elem[1:])
