def multiply(x, y):
    """ using 2 arguments only in the function"""
    print (x * y)

multiply(5, 4)

def multiply(*args):
    """ implementing *args to allow undefined number of args to be used in the code """
    b = 1
    for num in args:
        b *= num
    print(b)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)