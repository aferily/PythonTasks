# https://edabit.com/challenge/LR98GCwLGYPSv8Afb

def pluralize(lst):
	plurals = set()
	for elem in set(lst):
		if lst.count(elem) > 1:
			plurals.add(f'{elem}s')
		else:
			plurals.add(elem)
	return plurals
print(pluralize(['1', '1', '2', '1s', '3']))