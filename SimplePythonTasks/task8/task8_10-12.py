# 8_10
squares = {num: num ** 2 for num in range(10)}
print(f'квадраты:\n{squares}', end='\n'*2)

# 8_11
odd = {num for num in range(10) if num % 2 == 1}
print(f'нечетные:\n{odd}', end='\n'*2)

# 8_12 вариант 1
print('0-9 вариант 1:')
for elem in ('Got {num_formated}'.format(num_formated = num) for num in range(10)):
    print(elem)

# 8_12 вариант 2
print('\n0-9 вариант 2:')
for elem in ('Got %d' % num for num in range(10)):
    print(elem)