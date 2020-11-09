this_set = {"apple", "banana", "cherry"}
print(this_set)
for x in this_set:
    print(x)

this_set.add("orange")

print(this_set)

this_set.update(["orange", "mango", "grapes"])

print(this_set)

# discard vs remove (remove raises an error if doesn't exist unlike discard)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

