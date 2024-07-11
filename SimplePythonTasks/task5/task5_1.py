import re

song = '''When an eel grabs your arm,
And it causes great harm,
That's - a moray!'''

m_words = [x.capitalize() for x in re.sub('^[a-zA-Z\']', ' ', song).split(' ') if x.startswith('m')]
print(f"Слова на 'm' c заглавной:\n{m_words}\n")

song_cap_m = ''.join([x.capitalize() if x.startswith('m') else x for x in re.split('([a-zA-Z]*[a-zA-Z])', song)])
print(f"Песня с заглавием слов на 'm':\n{song_cap_m}")
