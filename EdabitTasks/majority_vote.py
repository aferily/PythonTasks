# https://edabit.com/challenge/pQavNkBbdmvSMmx5x

# 1
def majority_vote(lst):
	vote_counter = {}
	for elem in lst:
		if elem in vote_counter:
			vote_counter[elem] += 1
		else:
			vote_counter[elem] = 1
	max_count = 0
	major = None
	for elem in list(vote_counter.items()):
		if elem[1] > max_count:
			max_count = elem[1]
			major = elem[0]
	if max_count <= len(lst) / 2:
		major = None
	return major

print(majority_vote([1, 2, 2, 2, 1]))

# 2
def majority_vote(lst):
	from collections import defaultdict
	vote_counter = defaultdict(int)
	for elem in lst:
		vote_counter[elem] += 1
	major = max(list(vote_counter.items()), key=lambda x: x[1], default=(0,0))
	if major[1] > len(lst) / 2:
		return major[0]
	else:
		return None

print(majority_vote([]))
