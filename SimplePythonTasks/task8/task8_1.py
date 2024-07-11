# 1 вариант
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

# 2 вариант
e2f = {}
e2f['dog'] = 'chien'
e2f['cat'] = 'chat'
e2f['walrus'] = 'morse'
print(e2f)

# 3 вариант
e2f = dict(dog = 'chien', cat = 'chat', walrus = 'morse')
print(e2f)

# 4 вариант
words = 'dog,chien,cat,chat,walrus,morse'
ws = [w for w in words.split(',')]
ws_keys = [ws[n] for n in range(len(ws)) if n % 2 == 0]
ws_vals = [ws[n] for n in range(len(ws)) if n % 2 == 1]
e2f = dict(zip(ws_keys, ws_vals))
print(e2f)