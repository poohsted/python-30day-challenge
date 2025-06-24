"""
Challenge: Sensor Data Analysis

Sensor Data (10x5):\n
[[...]] # Your random 10x5 array here

Average temperature per sensor: [...] # 5 values
Min temperature per time point: [...] # 10 values
Overall standard deviation: [...] # single value

Readings above threshold (28):\n
[[False False True ...]
...] # Your boolean array here

Outlier temperatures: [...] # List of actual temperatures > 28

Reshaped data (25x2) shape: (25, 2)
Reshaped data:\n
[[...]] # Your 25x2 array here

"""

import numpy as np

sensor_data = np.random.randint(10, 31, size=(10,5))
print(f"Sensor Data (10x5):\n{sensor_data}")

average_per_sensor = np.mean(sensor_data, axis=0)
print(f"\nAverage temperature per sensor: {average_per_sensor.round(2)}")

min_per_timepoint = np.min(sensor_data, axis=1)
print(f"Min temperature per time point: {min_per_timepoint}")

overall_std = np.std(sensor_data)
print(f"Overall standard deviation: {overall_std:.2f}")

threshold = 28
above_threshold_mask = sensor_data > threshold
print(f"\nReadings above threshold ({threshold}) mask:\n{above_threshold_mask}")

outlier_temperatures = sensor_data[above_threshold_mask]
print(f"Outler temperatures: {outlier_temperatures}")

reshaped_data = sensor_data.reshape(25, 2)
print(f"\nReshaped data (25x2) shape: {reshaped_data.shape}")
print(f"Reshaped data:\n{reshaped_data}")

print("\n--- End Day 12 Challenge ---")