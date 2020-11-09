try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
    print("The 'try except' is finished")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
