# Task 1
# List Comprehensions
def task1():
    squares = [number * number for number in range(10)]
    return squares


# Task 2
# Functions
def task2():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    squares = [number * number for number in range(start, end + 1)]
    return squares

    # Task 3
    # Classes
    # class SquareGenerator:
    start = 0
    end = 0

    def __init__(self):
        self.start = int(input("Enter the start of the range: "))
        self.end = int(input("Enter the end of the range: "))

    def task3(self):
        squaresList = [number * number for number in range(self.start, self.end + 1)]
        return squaresList


# Task 4
# Libraries
import math


def square_root_generator(squaresList):
    squareRootList = [math.sqrt(number) for number in squaresList]
    return squareRootList


# Task 5
# Exceptions
def task5():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    try:
        if start > end:
            raise ValueError("Start must be less than end")
        squares = [number * number for number in range(start, end + 1)]
        return squares
    except ValueError:
        print("The start of the range cannot be bigger than the end of it!")


# Task 6
# Modules

# Created a separate module named squared_generator.py

# Task 7
# Packages

# Refactored my module using PyCharm into a Package called square_generator

# Task 8
# Inheritance
import square_generator as sq


class CubicGenerator(sq.SquareGenerator):
    def __init__(self):
        super().__init__()

    def task8(self):
        cubesList = [number ** 3 for number in range(self.start, self.end + 1)]
        return cubesList


# Task 9
# Function Overriding
class CubicGenerator(sq.SquareGenerator):
    def task8(self):
        try:
            if self.start > self.end:
                raise ValueError("Start must be less than end")
            cubesList = [number ** 3 for number in range(self.start, self.end + 1)]
            return cubesList
        except ValueError:
            print("The start of the range cannot be bigger than the end of it!")

# Task 10


# Test the function
if __name__ == "__main__":
    cg = CubicGenerator()
    cubes = cg.task8()
    print(cubes)
