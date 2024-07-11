# 8_3
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
f2e = {elem[1]: elem[0] for elem in e2f.items()}
print(f2e)

# 8_4
print(f2e['chien'])

# 8_5
e_words = ', '.join(list(e2f.keys()))
print(f'english words: {e_words}')