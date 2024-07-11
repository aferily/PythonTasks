class Device:
    def __init__(self, outcome) -> None:
        self.__outcome = outcome

    def does(self):
        return self.__outcome
    
class Laser(Device):
    def __init__(self) -> None:
        super().__init__('disintegrate')

class Claw(Device):
    def __init__(self) -> None:
        super().__init__('crush')

class SmartPhone(Device):
    def __init__(self) -> None:
        super().__init__('ring')

class Robot(Device):
    def __init__(self, *elements) -> None:
        self.__elements = elements
    
    def does(self):
        return ', '.join([elem.does() for elem in self.__elements])


my_robot = Robot(
    Laser(),
    Claw(),
    SmartPhone()
)
print(my_robot.does())