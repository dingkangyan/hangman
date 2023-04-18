class Shape():
    def __init__(self,w,l):
        self.width=w
        self.len=l

    def print_square(self):
        print("square is {}".format(self.width*self.len))
class Square(Shape):
    pass
ashape=Shape(20,10)
ashape.print_square()
