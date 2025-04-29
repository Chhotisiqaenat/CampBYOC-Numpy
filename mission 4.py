import numpy as np
import matplotlib.pyplot as plt

# Example atmospheric pressure data (in Pascals) from Mission 1
pressure_data = np.array([1,2,3,4,1000, 1200, 800, 1500, 950, 1100, 850, 1300, 1350, 1450, 
                          1050, 1400, 1220, 1150, 1400, 1000, 1250, 800, 900, 950])

# 1. Calculate Oxygen Levels using the formula: Oxygen Level = Pressure / 50
oxygen_levels = pressure_data / 50

# 2. Check for risky oxygen levels below 3% (i.e., below 0.03 oxygen level)
threshold = 0.03

if np.any(oxygen_levels < threshold):
        print("Warning: Some oxygen levels are below the safe threshold!")
        risky_indices = np.where(oxygen_levels < threshold)[0]
        for idx in risky_indices:
            print(f"Risky zone at index {idx}: Pressure = {pressure_data[idx]} Pa, Oxygen Level = {oxygen_levels[idx]:.3f}")
else:
    print("All oxygen levels are above the safe threshold.")


# 5. Plot Pressure vs Oxygen Level
plt.figure(figsize=(8, 6))
plt.plot(pressure_data, oxygen_levels, marker='o', color='b', linestyle='-', label="Pressure vs Oxygen Level")
plt.title("Pressure vs Oxygen Level")
plt.xlabel("Pressure (Pa)")
plt.ylabel("Oxygen Level (O2/50)")
plt.grid(True)
plt.legend()
plt.show()
