# Сортировка выбором. [O(n*n)]
# Эта функция возвращает индекс наименьшего элемента в списке.

def smallest_value(arr_to_sort):
    smallest = arr_to_sort[0]
    smallest_index = 0
    for i in range(1, len(arr_to_sort)):
        if arr_to_sort[i] < smallest:
            smallest_index = i
            smallest = arr_to_sort[i]
    return smallest_index


# Эта функция возвращает этот список отсортированный по возрастанию.

def selection_sort(arr_to_sort):
    new_list = []
    for i in range(len(arr_to_sort)):
        smallest = smallest_value(arr_to_sort)
        new_list.append(arr_to_sort.pop(smallest))
    return new_list
