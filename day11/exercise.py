# Today's Challenge: Robot Navigation Calculation
# Your challenge is to perform a fundamental robotics calculation: finding the distance between a robot's current position and its target destination.

# In 2D or 3D space, this is calculated using the Euclidean distance formula. For two points $P_1 = (x_1, y_1, z_1)$ and $P_2 = (x_2, y_2, z_2)$, the formula is:

# $Distance = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$

# This looks complex, but with NumPy's vectorized operations, it becomes beautifully simple.

# Your Task:

# Represent Positions: Create two NumPy arrays, robot_current_pos and robot_target_pos, to represent two points in 3D space.

# Current Position: (x=2, y=4, z=1)
# Target Position: (x=8, y=10, z=2)
# Calculate the Difference: Create a new vector called displacement by simply subtracting the robot_current_pos from robot_target_pos. NumPy will handle the element-wise subtraction.

# Calculate Squared Differences: Square the displacement vector. Again, NumPy will do this for every element.

# Sum and Square Root: Sum the elements of the squared displacement vector and then find the square root of that sum. You can use np.sum() and np.sqrt().

# Encapsulate in a Function: Put all this logic into a function called calculate_euclidean_distance(pos1, pos2) that takes two NumPy arrays and returns the final distance.

import numpy as np

def calculate_euclidean_distance(pos1, pos2):
    """
    Calculates the Euclidean distance between two points in N-dimensional space.
    
    Args:
        pos1 (np.ndarray): The first position vector.
        pos2 (np.ndarray): The second position vector.
        
    Returns:
        float: The Euclidean distance.
    """
    # Step 1: Calculate the element-wise difference (displacement vector)
    displacement = pos2 - pos1
    print(f"Displacement vector: {displacement}")

    # Step 2: Square the elements of the displacement vector
    squared_displacement = displacement ** 2 # Or np.square(displacement)
    print(f"Squared displacement: {squared_displacement}")

    # Step 3: Sum the squared differences
    sum_of_squares = np.sum(squared_displacement)
    print(f"Sum of squares: {sum_of_squares}")

    # Step 4: Calculate the square root of the sum
    distance = np.sqrt(sum_of_squares)
    
    return distance

# --- Main execution block ---
if __name__ == "__main__":
    # Define the robot's current and target positions as NumPy arrays
    robot_current_pos = np.array([2, 4, 1])
    robot_target_pos = np.array([8, 10, 2])

    print(f"Robot Current Position: {robot_current_pos}")
    print(f"Robot Target Position: {robot_target_pos}")
    print("-" * 30)

    # Call the function to get the distance
    dist = calculate_euclidean_distance(robot_current_pos, robot_target_pos)

    print("-" * 30)
    # The linalg.norm function is the "pro" way to do this, let's use it to check our answer!
    pro_way_distance = np.linalg.norm(robot_current_pos - robot_target_pos)

    print(f"Calculated Distance: {dist:.4f} units")
    print(f"Distance using np.linalg.norm (for verification): {pro_way_distance:.4f} units")

