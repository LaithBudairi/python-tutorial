print("Hello")
print('Hello')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# strings are arrays

a = "Hello, World!"
print(a[1])

# slicing
b = "Hello, World!"
print(b[2:5])

# negative indexing
b = "Hello, World!"
print(b[-5:-2])

# string length
a = "Hello, World!"
print(len(a))

# string methods

a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# we cannot concatenate numbers with string so we use format method
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."

# bool False values

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

