def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function():
    pass


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
