# parent class creation
class Person:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def print_name(self):
        print(self.first_name, self.last_name)


x = Person("Laith", "Budairi")
x.print_name()


# child class creation, init function overrides the parent function, unless you call the parent init to keep inheritance
class Student(Person):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)

    def print_name(self):
        print("yes")
        super().print_name()


x = Student("John", "Doe")
x.print_name()
