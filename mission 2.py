import numpy as np
import matplotlib.pyplot as plt

temps_celsius = np.array([-20, -15, -10, -5, 0, 5, 10])
print("Celcius tempts: ", temps_celsius)
temps_fahrenheit = (temps_celsius * 9/5) + 32
print("Fahrenheit temps:", temps_fahrenheit)

max_temp = np.max(temps_fahrenheit)
min_temp = np.min(temps_fahrenheit)

print("Highest temperature (F):", max_temp)
print("Lowest temperature (F):", min_temp)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Combine as structured data
temperature_data = np.column_stack((days, temps_celsius, temps_fahrenheit))

for row in temperature_data:
    print(f"{row[0]}: {row[1]}°C / {row[2]}°F")

plt.figure(figsize=(8, 5))
plt.plot(days, temps_fahrenheit, marker='o')
plt.title("Temperature Trend Over the Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°F)")
plt.grid(True)
plt.tight_layout()
plt.show()
