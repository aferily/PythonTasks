# https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb

# 1
def consecutive_combo(lst1, lst2):
    lst = lst1 + lst2
    lst.sort()
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1] + 1:
            return False
    return True
print(consecutive_combo([1,3],[4,2]))

# 2
def consecutive_combo(lst1, lst2):
    st = set(lst1) | set(lst2)
    print(st)
    return True
print(consecutive_combo([1,2,3],[4]))