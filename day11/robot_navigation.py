import numpy as np

# Representing a point (x, y ,z)
robot_position = np.array([0.5, 1.2, 0.3])
print(f"Robot's 3D position vector: {robot_position}")

# A matrix of weights for a small neural network layer (3 neurons, 2 inputs each)
weights = np.zeros((3, 2)) # Create a 3x2 matrix of zeros.
print(f"Initial weights matrix:\n{weights}")

# Simulate 10 distance sensor reading for 0 to 5 meters.
sensor_readings = np.linspace(0, 5, 10) # 10 evely spaced points between 0 to 5 meters.
print(f"Simulated sensor readings: {sensor_readings}")