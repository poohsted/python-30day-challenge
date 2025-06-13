robot = {
    "id" : 101,
    "specs": {
        "battery": "Li-ion",
        "camera": "HD",
        "sensors": ["Lidar","Ultrasonic"]
    }
}

print(robot["specs"]["camera"])

# Update values
robot["specs"]["camera"] = "4K"

# Delete a key
del robot["id"]

# Check if a key exists
if "sensors" in robot["specs"]:
    print("Sensors are present.")
