# https://edabit.com/challenge/AvP94XqJvPjoMk5PT

def unique_styles(albums):
	styles = set()
	for album in albums:
		styles = styles | set(album.split(','))
	return len(styles)