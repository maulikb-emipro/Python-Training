import time


def calc_time(func):
    """
    func :- decorator for checking the time is consumed by function.
    param :- function.
    returns :- wrapper for the function.
    """
    def wrapper(*args):
        """
        func :- wrapper function to check consuming time and to call the function.
        param :- passed parameters for functions.
        returns :- returns message of consumed time.
        """
        start=time.time()
        result=func(*args)
        end=time.time()
        print(func.__name__,"took",str((end-start)*1000),"milliseconds.")
        return result
        
    return wrapper

@calc_time
def calc_square(numbers):
    """
    func :- calculates square of all numbers given in array.
    param :- array of numbers.
    returns :- array of square of numbers.
    """
    result=[]
    for number in numbers:
        yield number^2
    yield "123"

@calc_time
def calc_cube(numbers):
    """
    func :- calculates square of all numbers given in array.
    param :- array of numbers.
    returns :- array of square of numbers.
    """
    result=[]
    for number in numbers:
        result.append(number^3)
    return result

array=range(0,10000)

abc=calc_square(array)
print(list(abc))
for a in abc:
    print(a,"1")
print(list(abc))
calc_cube(array)


