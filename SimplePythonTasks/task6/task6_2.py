guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
        number += 1
        continue
    elif number > guess_me:
        print("oops")
    else:
        print("found it!")
    break