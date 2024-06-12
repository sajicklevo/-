def double(function):
    def inner(argument):
        return function(function(argument))
    return inner
def multiply_by_five(x):
    return x*5
print(double(multiply_by_five)(3))
