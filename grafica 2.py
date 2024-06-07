import numpy as np
import matplotlib.pyplot as plt
def f(x):
    #return (1+x**2)
   return np.cos(x**2)

x = np.linspace(0, 2, 100)
y = f(x)
x_fill = np.linspace(0, 2, 100)  
y_fill = f(x_fill)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) (cos(x^2)')



plt.title('Gráfica de f(x) = cos(x**2) sin relleno')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='blue',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()