import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches

def twoBodyProblem(start, t):
    mu = 3.986004418E+05
    x = start[0]
    y = start[1]
    x_dot = start[2]
    y_dot = start[3]
    x_ddot = -mu * x / (x ** 2 + y ** 2) ** (3 / 2)
    y_ddot = -mu * y / (x ** 2 + y ** 2) ** (3 / 2)
    dstate_dt = [x_dot, y_dot, x_ddot, y_ddot]
    return dstate_dt

# Initial Conditions
X_0 = 0  # [km]
Y_0 = -5500  # [km]
VX_0 = 9.8  # [km/s]
VY_0 = 0 # [km/s]
state_0 = [X_0, Y_0, VX_0, VY_0]

t = np.linspace(0, 4*3600, 700)

sol = odeint(twoBodyProblem, state_0, t)
X_Sat = sol[:, 0]
Y_Sat = sol[:, 1]

fig, ax = plt.subplots()
ax.set_aspect('equal')

#plt.plot(X_0, Y_0, 'r*')
#plt.plot(X_Sat, Y_Sat)

N = 50
phi = np.linspace(0, 2 * np.pi, N)
r_Earth = 4378.14
X_Earth = r_Earth * np.cos(phi)
Y_Earth = r_Earth * np.sin(phi)
ax.plot(X_Earth, Y_Earth, color='green')
ax.plot(X_Sat, Y_Sat, color='blue')
ax.plot(X_0,Y_0,'r*')

plt.title('Orbit Simulation')
plt.xlabel('km')
plt.ylabel('km')
red_patch = mpatches.Patch(color='blue', label='Umlaufbahn')
ax.legend(handles=[red_patch])
plt.show()
