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

def some_args(arg_1, arg_2, arg_3):
    """ Here we are using *args to pass arguments into functions """
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

args = ("Sammy", "Casey", "Alex")
some_args(*args)