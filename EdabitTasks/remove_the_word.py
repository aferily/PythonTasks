# https://edabit.com/challenge/gH3QMvF3czMDjENkk

# 1
def remove_letters(letters, word):
	from collections import defaultdict
	letters_counter = defaultdict(int)
	for letter in letters:
		letters_counter[letter] += 1
	for letter in word:
		if letter in letters_counter:
			letters_counter[letter] -= 1
	res_list = []
	for item in list(letters_counter.items()):
		res_list += [item[0]] * item[1]
	return sorted(res_list)
print(remove_letters(["b", "b", "b", "b", "a"],'bb'))

# 2
def remove_letters(letters, word):
	for letter in word:
		letters.remove(letter)
	return sorted(letters)
letters = ["b", "b", "b", "b", "a"]
print(remove_letters(letters.copy(),'bb'))