class Element():
    def __init__(self, name, symbol, number) -> None:
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name
    
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f'name: {self.name}\nsymbol: {self.symbol}\nnumber: {self.number}'

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)

print(f'name: {hydrogen.name}')