# https://edabit.com/challenge/BuwHwPvt92yw574zB

step = 7
count = 3

# 1
list_of_mult = list(range(step, step * count + 1, step))
print(list_of_mult)

# 2
list_of_mult = [step * i for i in range(1, count + 1)]
print(list_of_mult)
