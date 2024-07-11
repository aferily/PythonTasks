# 10_4
class Element():
    def __init__(self, name, symbol, number) -> None:
        self.name = name
        self.symbol = symbol
        self.number = number

    def __repr__(self) -> str:
        return f'name: {self.name}\nsymbol: {self.symbol}\nnumber: {self.number}'

hydrogen = Element('Hydrogen', 'H', 1)
print(f'hydrogen:\n{hydrogen}')

# 10_5
element_desc = {
    'name': 'Hydrogen',
    'symbol': 'H', 
    'number': 1
    }

hydrogen = Element(**element_desc)
print(f'hydrogen:\n{hydrogen}')