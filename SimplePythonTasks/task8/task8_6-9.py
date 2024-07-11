e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

# 8_6
cats = ['Henri', 'Grumpy', 'Lucy']
animals = {'cats': cats, 'octopi': {}, 'emus': {}}
life = {'animals': animals, 'plants': {}, 'other': {}}
print(f'life:\n{life}\n')

# 8_7
print(f'высокоуровневые ключи life:\n{list(life.keys())}\n')

# 8_8
print(f'ключи life["animals"]:\n{list(life['animals'].keys())}\n')

# 8_9 вариант 1
print(f'life["animals"]["cats"]:\n{life["animals"]["cats"]}\n')

# 8_9 вариант 2 (без исключения при пустых животных)
print(f'life["animals"]["cats"]:\n{life["animals"].get('cats', 'no cats')}\n')