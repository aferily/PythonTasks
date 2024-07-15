# https://edabit.com/challenge/GaJkMnuHLuPmXZK7h

def letters(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    return list(map(lambda x: ''.join(sorted(list(x))), [
        set1 & set2,
        set1 - set2,
        set2 - set1
    ]))