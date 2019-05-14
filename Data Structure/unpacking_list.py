numbers = [1, 2, 3]
number_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# varibale should be equal in number both side
first, second, third = numbers
first_num, second_num, *other_num = number_test
print(first)
print(second)
print(first_num)
print(second_num)
print(other_num)

first_number, *other_number, last_number = number_test
print(first_number, last_number)
print(other_number)
