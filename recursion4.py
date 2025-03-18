def reverse(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse(lst[:-1])
lst = [1, 2, 3, 4, 5]
print(reverse(lst))