# 7_1
init_year = 1998
year_list_len = 6

# 1 вариант
years_list = [num + init_year for num in range(0, year_list_len)]
print(years_list)

# 2 вариант
years_list = list(range(init_year, init_year + year_list_len))
print(years_list)

# 3 вариант
years_list = list()
for year in range(init_year, init_year + year_list_len):
    years_list.append(year)
print(years_list)

# 7_2
birthyear_num = 3
print(f"{birthyear_num}-й день рождения в {years_list[birthyear_num]}")

# 7_3
print(f"максимальное число лет в году из списка: {years_list[-1:][0]}")

# 7_4
things = ["mozzarella", "cinderella", "salmonella"]

# 7_5
things[1] = things[1].capitalize()
print(things)

# 7_6
things[0] = things[0].upper()
print(things)

# 7_7
local_thing = things.copy()
local_thing.remove('salmonella')
print (local_thing)

local_thing = things.copy()
del local_thing[2]
print(local_thing)

# 7_8
surprise = ["Groucho", "Chico", "Harpo"]

# 7_9
new_element = surprise[-1:][0].lower()[::-1].capitalize()
print(new_element)

# 7_10
even = [num for num in range(10) if num % 2 == 0]
print(even)

even = [num for num in range(0, 10, 2)]
print(even)

# 7_11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"

for (first, second) in rhymes:
    for start1_elem in start1:
        print(f"{start1_elem.capitalize()}", end = "! ")
    print(f"{first.capitalize()}!")
    print(f"{start2} {second}.", end = "\n\n")
