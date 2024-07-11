class Element():
    def __init__(self, name, symbol, number) -> None:
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'name: {self.name}\nsymbol: {self.symbol}\nnumber: {self.number}')

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()