# day9_file_io_part2.py

from datetime import datetime

def append_note(filename, note):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    with open(filename, 'a') as file:
        file.write(f"{timestamp} {note}\n")

def read_notes(filename):
    with open(filename, 'r') as file:
        return file.readlines()

if __name__ == "__main__":
    filename = "notes_log.txt"

    note = input("Write a note for today: ")
    append_note(filename, note)

    print("\n All Notes:")
    for line in read_notes(filename):
        print("- " + line.strip())
