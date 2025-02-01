import numpy as np
import matplotlib.pyplot as plt

chewing_force = 100
angle = 45
number_of_teeth = 12
vertical_component = lambda x : chewing_force * np.sin(np.radians(x))  
horizontal_component = lambda x : chewing_force * np.cos(np.radians(x))
A_d = [15.0, 20.0, 18.0, 25.0, 30.0, 35.0, 40.0, 35.0, 30.0, 25.0, 18.0, 15.0]
r_d = [10, 12, 14, 16, 18, 20, 22, 20, 18, 16, 14, 12]
r_sum = sum(r_d)
# calculated forces and pressures
F_d = [round(chewing_force *r / r_sum,2) for r in r_d]
P_d = [round(force / area ,2) for force,area in zip(F_d,A_d)]

# print answers
print(f'Vertical Component {vertical_component(angle)}') 
print(f'Horizontal Component {horizontal_component(angle)}')
print("Force on each tooth :\n")
for i,force in enumerate(F_d,1):
    print(f'    Tooth {i} : {force}')
print("Pressure on each tooth :\n")    
for i,pressure in enumerate(P_d,1):
    print(f'    Tooth {i} : {pressure}')

# force 
plt.figure(figsize=(10, 5))
plt.bar(range(1, number_of_teeth + 1), F_d, color='blue')
plt.title("Force Distribution Across Teeth")
plt.xlabel("Tooth Number")
plt.ylabel("Force (N)")
plt.xticks(range(1, number_of_teeth + 1))
plt.grid(axis='y')
plt.show()
# pressure
plt.figure(figsize=(10, 5))
plt.bar(range(1, number_of_teeth + 1), P_d, color='green')
plt.title("Pressure Distribution Across Teeth")
plt.xlabel("Tooth Number")
plt.ylabel("Pressure (N/mm²)")
plt.xticks(range(1, number_of_teeth + 1))
plt.grid(axis='y')
plt.show()