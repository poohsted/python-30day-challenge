# Exercise: Robot Battery Monitor with Real-Time Countdown

# Scenario:
# You're building a robot health-check system. When the robot's battery is low, it enters power-saving mode and starts a countdown until shutdown unless recharged.

# 🧠 Tasks:
# Create a robot dictionary with:

# name

# battery (in %)

# status (e.g. "active", "power-saving", "shutting down")

# Check the battery:

# If it's below 30%, set status to "power-saving".

# In power-saving mode:

# Print a countdown from 5 to 1 using time.sleep(1)

# After countdown, print "System shutting down..."

# Bonus 💥: Let user input a number to simulate charging and update battery status.

import time

robot = {
    "name": "K-LONG-01",
    "battery": 12,
    "status": "active"
}

if robot["battery"] < 30:
    robot["status"] = "power saving"
    print(f"Status: {robot['status']}")

    seconds = 5
    print("Countdown to shutdown:")
    for i in range(seconds, 0, -1):
        print(f"{i}")
        time.sleep(1)

    print("System shutting down...")

else:
    print("Battery is good. System is running normally.")
