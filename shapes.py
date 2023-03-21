
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

class square(rectangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width

if __name__ == '__main__':
    rect = square(5,6)
    print(rect.area())