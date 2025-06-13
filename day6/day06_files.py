person = {
    "name": "Pooh",
    "age": 21,
    "skills": ["Python", "Robotics", "Music"]
}

print(person["name"])
print(person.get("skills"))

# Add a new key
person["hobby"] = "Singing"

# Loop through keys & values
for key, value in person.items():
    print(key, "=>", value)