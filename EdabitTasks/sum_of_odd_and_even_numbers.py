# https://edabit.com/challenge/5XXXppAdfcGaootD9

elements = [1, 2, 3, 4]

# 1
sum_odd = sum([elem for elem in elements if elem % 2 != 0])
sum_even = sum([elem for elem in elements if elem % 2 == 0])
print(f'1. sum odd: {sum_odd}, sum_even: {sum_even}')

# 2 
sum_even = 0
sum_odd = 0
for elem in elements:
    if elem % 2 == 0:
        sum_even += elem
    else:
        sum_odd += elem
print(f'2. sum odd: {sum_odd}, sum_even: {sum_even}')
