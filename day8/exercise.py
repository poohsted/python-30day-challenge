# 🔧 Instructions:
# Use a while loop to simulate battery draining.

# Inside, use a for loop to simulate tasks being executed.

# Robot stops if battery < 10.

# Use break, continue, and maybe else in your logic.

import time

robot = {
    "name": "K-LONG-01",
    "battery": 50,
    "status": "active"
}

tasks = ["scan", "move", "report"]

while robot["battery"] > 0:
    print(f"\n🔋 Battery: {robot['battery']}%")

    if robot["battery"] < 10:
        print("⚠️ Battery too low. Shutting down...")
        robot["status"] = "shutdown"
        break

    for task in tasks:
        if robot["battery"] < 10:
            print("⚠️ Battery drained mid-task. Aborting...")
            break
        print(f"  🔧 Performing task: {task}")
        time.sleep(0.5)
        robot["battery"] -= 5
        if task == "report" and robot["battery"] > 30:
            print("  ✅ Mission running smoothly.")
            continue  # Just for demo purposes

    else:
        print("✅ All tasks completed for this cycle.")

    time.sleep(0.5)

print("\n💤 System status:", robot["status"])
