# Бинарный поиск. [O(log n)]

def binary_search(arr, num):
    left_border = 0
    right_border = len(arr) - 1
    while left_border <= right_border:
        middle_value = (left_border + right_border) // 2
        guess = arr[middle_value]
        if guess == num:
            return middle_value
        if guess > num:
            right_border = middle_value - 1
        else:
            left_border = middle_value + 1
    return None
