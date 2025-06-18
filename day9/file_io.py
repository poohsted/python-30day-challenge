# day9_file_io.py

def write_file(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + 'n')

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()
    
if __name__ == "__main__":
    filename = "notes.txt"
    lines = [
        "This is Day 9 of Python Challenge!",
        "We are learning how to write and read files."
        "This file was created using Python."
    ]

    write_file(filename, lines)
    content = read_file(filename)
    
    print("File content:")
    for line in content:
        print(line.strip())
