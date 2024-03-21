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
class SquareGenerator:
    start = 0
    end = 0

    def __init__(self):
        self.start = int(input("Enter the start of the range: "))
        self.end = int(input("Enter the end of the range: "))

    def task3(self):
        squaresList = [number * number for number in range(self.start, self.end + 1)]
        print(squaresList)


# Task 4


# Task 5


# Task 6


# Task 7


# Task 8


# Task 9


# Task 10


# Test the function
if __name__ == "__main__":
    sq1 = SquareGenerator()
    sq1.task3()
