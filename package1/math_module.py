from .exceptions import InvalidValueException
class BasicMath:
    def add(self, number1: int, number2: int) -> int:
        return number1 + number2
    
    def subtract(self, number1: int, number2: int) -> int:
        return number1 - number2
    
    def multiply(self, number1: int, number2: int) -> int:
        return number1 * number2
    
    def divide(self, number1: int, number2: int) -> float:
        if number2 == 0:
            raise InvalidValueException
        return number1 / number2


if __name__ == "__main__":
    bm = BasicMath()
    print(bm.divide(5,0))