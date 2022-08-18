# Быстрая сортировка, используя рекурсию. [O(n*log n)]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        start_element = arr[0]
        less_start_element = [i for i in arr if i < start_element]
        greater_start_element = [i for i in arr if i > start_element]
        return quick_sort(less_start_element) + [start_element] + quick_sort(greater_start_element)
