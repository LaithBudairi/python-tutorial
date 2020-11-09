my_list = ["apple", "banana", "cucumber", "carrot"]
print(my_list)
print(my_list[2:4])
print(my_list[:3])

my_list[1] = "blueberry"
print(my_list)

for x in my_list:
    print(x)

if "apple" in my_list:
    print("Yes, 'apple' is in the fruits list")

print(len(my_list))

my_list.append("orange")
print(my_list)

my_list.insert(1, "orange")

print(my_list)

del my_list[0]
print(my_list)

# del can also delete list completely


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

print(list1)
