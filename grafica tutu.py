import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x + 1
x = np.linspace(2, -2, 400)

y = f(x)

plt.plot(x, y, 'b', label='f(x) = x + 1')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x) = x + 1')

plt.grid(True)
plt.legend()
plt.show()