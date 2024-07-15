# https://edabit.com/challenge/2zKetgAJp4WRFXiDT

num = 124

# 1
print(len(str(num)))

# 2
num_copy = num
counter = 0 if num_copy != 0 else 1 
while num_copy != 0:
    num_copy = num_copy // 10
    counter += 1
print(counter)