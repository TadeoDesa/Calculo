import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x + x**3 + 4) / 3

a = -2
b = 2

g_constant = (b**3 - a**3) / 3

x = np.linspace(-10, 10, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = (x + x^3 + 4) / 3')

x_fill = np.linspace(a, b, 200)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4, label='Área bajo f(x)')

plt.axhline(g_constant, color='green', linestyle='--', linewidth=2, label=f'g(x) = (b^3 - a^3) / 3 = {g_constant:.2f}')

plt.title('Gráfica de f(x) y constante g(x)')
plt.xlabel('x')
plt.ylabel('f(x) / g(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
