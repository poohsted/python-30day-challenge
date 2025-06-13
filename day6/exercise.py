# RoboProfile Generator

# 1. Create a dictionary called robot_profile with:

# | Key        | Value (example)                                       |
# | `name`     | `"K-LONG-01"`                                         |
# | `type`     | `"Autonomous Delivery"`                               |
# | `battery`  | `92` (integer, as percent)                            |
# | `sensors`  | A list: `["Lidar", "Camera", "GPS"]`                  |
# | `settings` | A nested dict with keys: `speed`, `volume`, `ai_mode` |

# 2. Write code that:

# 📤 Prints all keys and values nicely formatted

# 🔋 If battery is below 20%, print: ⚠️ Low battery! Please recharge.

# ➕ Adds a sensor "Infrared" only if it’s not already there

# 🧹 Deletes the "volume" setting from the settings dict

# 🔁 Loops through sensors and prints:
# "Sensor active: Lidar"
# "Sensor active: Camera" etc.

# 📦 Uses a set to show what sensors are unique between two robots (compare robot_profile["sensors"] with another list)

robot_profile = {
    "name": "K-LONG-01",
    "type": "Autonomous Delivery",
    "battery": 19,
    "sensors": ["Lidar", "Camera", "GPS"],
}

print(robot_profile["name"])
print(robot_profile["type"])
print(robot_profile["battery"])
print(robot_profile.get("sensors"))

if robot_profile["battery"] < 20:
    print("Low battery! Please recharge.")

if "Infrared" not in robot_profile["sensors"]:
    robot_profile["sensors"].append("Infrared")

robot_profile["settings"] = {
    "speed": "normal",
    "volume": "medium",
    "ai_mode": "Autonomous"
}

del robot_profile["settings"]["volume"]

for sensor in robot_profile["sensors"]:
    print(f"Sensor active: {sensor}")

other_robot_sensors = ["Radar", "Camera", "GPS"]
unique_sensors = set(robot_profile["sensors"]).symmetric_difference(other_robot_sensors)
print(f"Unique sensors between the two robots: {unique_sensors}")

# Bonus function:
def summarize_robot(profile: dict):
    print("\n[Robot Summary]")
    print(f"Name: {profile['name']}")
    print(f"Type: {profile['type']}")
    print(f"Battery: {profile['battery']}%")
    print("Sensors: " + ", ".join(profile["sensors"]))
    print("AI Mode: " + profile["settings"]["ai_mode"])

summarize_robot(robot_profile)