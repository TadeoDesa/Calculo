import matplotlib.pyplot as plt
import numpy as np

# Definir los valores de x y h
x = 1  # Puedes cambiar este valor
h = 2  # Puedes cambiar este valor

# Definir las funciones A(x) y A(x + h)
def A(x):
    return x**3  # Ejemplo de función A(x), puedes cambiarla según necesites

# Coordenadas de los puntos P1 y P2
P1 = (x, A(x))
P2 = (x + h, A(x + h))

# Valores de x para graficar
x_vals = np.linspace(x - h, x + h, 400)

# Valores de y para graficar A(x)
y_vals = A(x_vals)

# Calcular la pendiente
m = (1 + 3*x*2 + 3*x*h + h*3) / 3

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la función A(x)
ax.plot(x_vals, y_vals, label='A(x)')

# Graficar los puntos P1 y P2
ax.plot(P1[0], P1[1], 'ro', label=f'P1 ({P1[0]}, {P1[1]:.2f})')
ax.plot(P2[0], P2[1], 'bo', label=f'P2 ({P2[0]}, {P2[1]:.2f})')

# Graficar la línea de la pendiente entre P1 y P2
x_line = np.array([P1[0], P2[0]])
y_line = P1[1] + m * (x_line - P1[0])
ax.plot(x_line, y_line, 'g--', label=f'Pendiente = {m:.2f}')

# Añadir leyenda y etiquetas
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('A(x)')
ax.set_title('Gráfica de A(x) con puntos P1 y P2 y su pendiente')

# Mostrar la gráfica
plt.grid(True)
plt.show()