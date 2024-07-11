class Thing2():
    letters = 'abc'

print(f'Thing2.letters: {Thing2.letters}')

example = Thing2()
Thing2.letters = '123'
print(f'example.letters: {example.letters}')