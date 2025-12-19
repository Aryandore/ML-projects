import numpy as np

v = np.array([1,2,5])
m = np.array([7,3,2])

print("Addition:", v + m)
print("Subtraction:", v - m)
print("Element-wise Multiplication:", v * m)
print("Element-wise Division:", v / m)
print("Dot Product:", np.dot(v, m))
print("Cross Product:", np.cross(v, m))
print("Magnitude of v:", np.linalg.norm(v))
print("Magnitude of m:", np.linalg.norm(m))
print("Angle between v and m (radians):", np.arccos(np.dot(v, m) / (np.linalg.norm(v) * np.linalg.norm(m))))
