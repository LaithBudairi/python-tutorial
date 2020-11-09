this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(this_dict)

x = this_dict["model"]
# or
x = this_dict.get("model")

this_dict["year"] = 2018

for x in this_dict:
    print(x)

this_dict["color"] = "red"
print(this_dict)

this_dict.pop("model")
print(this_dict)

# nested dictionaries
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
