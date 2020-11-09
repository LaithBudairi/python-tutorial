try:
    f = open("myFile.txt")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
    f.close()
