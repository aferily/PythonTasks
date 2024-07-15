from pprint import pprint
from collections import OrderedDict, defaultdict

# 11_5
plain = {
    'a': 1,
    'b': 2,
    'c': 3
}
pprint(plain)

# 11_6
fancy = OrderedDict(plain)
pprint(fancy)

# 11_7
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')

