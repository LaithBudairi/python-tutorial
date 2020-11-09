import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x.group())  # this will print an object
