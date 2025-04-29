import numpy as np
import matplotlib.pyplot as plt

# 1. Generate a 5x5 NumPy array with random elevation values between 100 and 500 meters
elevation_data = np.random.randint(100, 501, size=(5, 5))

# 2. Find the highest point on the planet
highest_point = np.max(elevation_data)

# 3. Sort each row in ascending order for terrain analysis
sorted_elevation_data = np.sort(elevation_data, axis=1)

# 4. Visualize the terrain findings using a line graph
plt.figure(figsize=(8, 6))
for i in range(5):
    plt.plot(sorted_elevation_data[i], label=f"Row {i + 1}")

plt.title("Terrain Elevation Analysis")
plt.xlabel("Columns")
plt.ylabel("Elevation (meters)")
plt.legend()
plt.grid(True)
plt.show()

# 5. Find flat areas: Challenge them to find any row/column with minimal elevation difference
row_differences = np.ptp(sorted_elevation_data, axis=1)  # Peak-to-peak (max - min) in each row
column_differences = np.ptp(sorted_elevation_data, axis=0)  # Peak-to-peak in each column

# Find rows or columns with minimal elevation difference
min_row_diff = np.min(row_differences)
min_column_diff = np.min(column_differences)

print("row difference: " , row_differences)
print("column differences: " , column_differences)
print("min row diff: " , min_row_diff)
print("min column diff: " , min_column_diff)

