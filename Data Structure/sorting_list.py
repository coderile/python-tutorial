number = [34, 78, 1, 45, 99, 10101, 20384, 67]

# returning new sorted list with modify existing list

sorted_list = sorted(number)
sorted_list_reverse = sorted(number, reverse=True)
print(sorted_list)
print(sorted_list_reverse)

# in Accesinding order with original list modification
number.sort()
print(number)

# in decending order with original list modification

number.sort(reverse=True)
print(number)


# List of tuples

items = [("product1", 10), ("product2", 20), ("product3", 9), ("product4", 2)]


def sort_item(items):
    return items[1]


items.sort(key=sort_item)
print(items)
