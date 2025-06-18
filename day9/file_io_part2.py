# day9_file_io_part2.py

def append_note(filename, note):
    with open(filename, 'a') as file:
        file.write(note + '\n')

def read_notes(filename):
    with open(filename, 'r') as file:
        return file.readlines()
    
if __name__ == "__main__":
    filename = "notes_log.txt"
    note = input("Write a note for today: ")
    append_note(filename, note)

    print("\n All notes:")
    for line in read_notes(filename):
        print("-" + line.strip())