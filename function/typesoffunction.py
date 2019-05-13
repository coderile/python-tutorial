# there are two types of function in python

# 1.> perform a  task
# 2.> return some value


def add(x, y):
    return x+y


def result(name):
    print(name)
    print(add(2, 3))


result('Amit')


# keyword Argument

def increment(number, by):
    return number+by


print(increment(2, by=1))


# default Argument

def testIncrement(number, by=1):
    return number+by


print(testIncrement(8, 5))


# All the parameter comes after all the required parameter
