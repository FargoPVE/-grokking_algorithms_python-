# Подсчет элементов, используя рекурсию. [O(n)]

def count_elements(list_of_elem):
    if len(list_of_elem) == 0:
        return 0
    else:
        return 1 + count_elements(list_of_elem[1:])
