# Факториал, используя рекурсию. [O(n)]

def factorial(integer):
    if integer == 1:
        return 1
    else:
        return integer * factorial(integer - 1)
