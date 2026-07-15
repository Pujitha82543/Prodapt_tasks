def write_file(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()

def read_file(filename):
    f = open(filename, "r")
    print(f.read())
    f.close()