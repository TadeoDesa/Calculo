import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 + x**2

x = np.linspace(-10, 10, 400)

y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = 1 + x^2', color='blue')

plt.title('Gráfica de f(x) = 1 + x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='red', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()