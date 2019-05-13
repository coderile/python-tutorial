def multipy(x, y):
    return x*y


print(multipy(2, 3))


# on above code only argument we can pass for n number of parameter we need to modify which we are doing below
# use single astrick

def multiplication(*numbers):
    total = 1
    print(numbers)
    for num in numbers:
        print(num)
        total = total*num
    return total


print(multiplication(1, 2, 3, 4))


# use of two astrick
# key value pair and its dictionary
def save_user(**user):
    print(user["id"])
    print(user)


save_user(id=1, name="john", sirname="doe", city="ny")
