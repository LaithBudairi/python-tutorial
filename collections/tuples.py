this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print(this_tuple[1])
for x in this_tuple:
    print(x)

this_tuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(this_tuple)

this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = this_tuple.count(5)
print(x)

x = this_tuple.index(8)

print(x)
