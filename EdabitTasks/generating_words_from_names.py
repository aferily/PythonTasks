# https://edabit.com/challenge/sDvjdcBrbHoXKvDsZ

def anagram(name, words):
    from functools import reduce
    clear_word = lambda x: x.lower().replace(' ', '')
    name_sorted = ''.join(sorted(clear_word(name))) 
    concat_words_sorted = ''.join(sorted(reduce(lambda acc, x: acc + clear_word(x), words)))
    return name_sorted == concat_words_sorted
print(anagram('Aw Rta', ['ta', 'rw' ,'a']))