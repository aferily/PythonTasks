# https://edabit.com/challenge/HrCuzAKE6skEYgDmf

def pairs(lst):
	pairs = []
	while len(lst):
		pairs.append([lst[0], lst[-1]])
		lst = lst[1:-1]
	return pairs

print(pairs([1, 2, 3, 4, 5]))