class C1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


o1 = C1("Laith", 22)
print(o1.name)
o1.birth = "ramallah"

print(o1.birth)

del o1.birth

print(o1.birth)  # error
