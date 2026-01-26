import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

alpha = 2.0
beta = 0.1
gamma = 1.5
delta = 0.075

def f_lotkavolterra(X, t):
    x, y = X
    dxdt = alpha * x - beta * x * y
    dydt = -gamma * y + delta * x * y
    dXdt = [dxdt, dydt]
    return dXdt

x0 = 40
y0 = 9

X0 = [x0, y0]

t = np.linspace(0, 15, 300)
X = odeint(f_lotkavolterra, X0, t)

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)
ax.plot(t, X[:, 0], 'b', label='Prey (x)')
ax.plot(t, X[:, 1], 'r', label='Predator (y)')
ax.set_xlabel('Time')
ax.set_ylabel('Population')
ax.legend()
plt.tight_layout()
plt.show()

fig.savefig('lotka_volterra_time_series.pdf')
