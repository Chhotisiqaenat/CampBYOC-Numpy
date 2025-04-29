import numpy as np
import matplotlib.pyplot as plt

# Original pressure readings and corresponding sensor IDs
pressure_readings = np.array([980, 1023, 45, 1980, 2075, 1500, 80, 1999, 3001, 1200,
                              999, 85, 1450, 1760, 90, 2005, 1050, 500, 1890, 2300,
                              30, 1700, 850, 2100, 1950])

sensor_ids = np.array([
    'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
    'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20',
    'S21', 'S22', 'S23', 'S24', 'S25'  
])

# Create boolean mask for valid pressure range
valid_mask = (pressure_readings >= 100) & (pressure_readings <= 2000)

# Filter valid readings and matching sensor IDs
valid_pressure = pressure_readings[valid_mask]
valid_sensor_ids = sensor_ids[valid_mask]

# Display results
print("Valid pressures:\n", valid_pressure)
print("Valid sensor IDs:\n", valid_sensor_ids)

# Statistics
average_pressure = np.mean(valid_pressure)
median_pressure = np.median(valid_pressure)
min_pressure = np.min(valid_pressure)
max_pressure = np.max(valid_pressure)

print("\n--- Pressure Stats ---")
print("Average:", average_pressure)
print("Median:", median_pressure)
print("Min:", min_pressure)
print("Max:", max_pressure)

# Divide into zones
zone_A = valid_pressure[0:5]
zone_B = valid_pressure[5:10]
zone_C = valid_pressure[10:15]

print("\n--- Zones ---")
print("Zone A:", zone_A)
print("Zone B:", zone_B)
print("Zone C:", zone_C)

# 4. Visualize the pressure readings from each zone using a line graph
plt.figure(figsize=(8, 6))

# Plot each zone
plt.plot(zone_A, label="Zone A", marker='o')
plt.plot(zone_B, label="Zone B", marker='s')
plt.plot(zone_C, label="Zone C", marker='^')

# Customizing the graph
plt.title("Pressure Readings from Different Zones")
plt.xlabel("Sensor Index")
plt.ylabel("Pressure (Pa)")
plt.legend()
plt.grid(True)

# Display the graph
plt.show()
