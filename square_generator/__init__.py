from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    start = 0
    end = 0

    def __init__(self):
        self.start = int(input("Enter the start of the range: "))
        self.end = int(input("Enter the end of the range: "))

    @abstractmethod
    def generate_squares(self):
        pass
