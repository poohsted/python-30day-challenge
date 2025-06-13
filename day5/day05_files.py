# Write to a text file
with open('example.txt', 'w') as file:
    file.write("This is Day 5 of the Python challenge.\n")
    file.write("Learning to work with files is essential.\n")

# Read from the text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

import csv

data = [
    ['Name', 'Age', 'City'],
    ['Pooh', 21, 'Bangkok'],
    ['Sora', 22, 'Tokyo']
]

# Write CSV file
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read CSV file
print("\mCSV file content:")
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import json

person = {
    "name": "Pooh",
    "age": 20,
    "skills": ["Python", "Robotics", "Music"]
}

# Write JSON file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Read JSON file
print("\nJSON file content:")
with open('person.json', 'r') as file:
    data = json.load(file)
    print(f"Name: {data['name']}")
    print(f"Skills: {', '.join(data['skills'])}")

