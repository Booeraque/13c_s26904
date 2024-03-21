class SquareGenerator:
    start = 0
    end = 0

    def __init__(self):
        self.start = int(input("Enter the start of the range: "))
        self.end = int(input("Enter the end of the range: "))

    def task3(self):
        squaresList = [number * number for number in range(self.start, self.end + 1)]
        return squaresList
