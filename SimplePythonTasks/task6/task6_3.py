guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
        continue
    elif number > guess_me:
        print("oop!")
    else:
        print("found it!")
    break