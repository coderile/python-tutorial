lettes = ["a", "b", "c", "d"]


# add


# at the last
lettes.append("e")
print(lettes)

# at the any index postion
lettes.insert(0, "-")
print(lettes)

# removing items

lettes.pop()
print(lettes)

lettes.pop(0)
print(lettes)

# first occurence or if we want to remove all occurence of b then we have to loop
lettes.remove("b")

del lettes[0:2]
print(lettes)

lettes.clear()
print(lettes)
