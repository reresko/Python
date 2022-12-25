#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


dt = 0.1 # s

g = 10 # m/s^2
x = 6378000 # m
v = 0 # m/s

# Parametry pro simulaci se třením
# při c_D = 0 je tření vypnuté
m = 60/1000 # kg
c_D = 0
# Odkomentujte pro zapnutí tření:
#c_D = 0.5
S = np.pi*(6.5/100/2)**2 # m^2
density = 1.125 # kg/m^3


vs = [v]
xs = [x]

while x > 0:
	F_d = -1/2 * c_D * S * density * v**2
	v += (g + F_d/m)*dt
	x -= v*dt
	vs.append(v)
	xs.append(x)

vs = np.array(vs)
xs = np.array(xs)
ts = np.arange(0, len(vs)*dt, dt)

print("Dopadová rychlost", vs[-1])
print("Doba pádu", ts[-1])

E_k = 1/2 * m * vs**2
E_p = m * g * xs
assert E_k[0] == 0
E_0 = E_k[0] + E_p[0]

fig, ax = plt.subplots(2, 2)

ax[0, 0].set_title("Okamžitá rychlost")
ax[0, 0].set_ylabel("v [m/s]")
ax[0, 0].set_xlabel("t [s]")
ax[0, 0].plot(ts, vs)

# Pro zobrazení pouze prvních 10s
#ax[0, 0].plot(ts[:100], vs[:100])

ax[0, 1].set_title("Výška")
ax[0, 1].set_ylabel("x [m]")
ax[0, 1].set_xlabel("t [s]")
ax[0, 1].plot(ts, xs)

ax[1, 0].set_title("Energie")
ax[1, 0].plot(ts, E_k)
ax[1, 0].plot(ts, E_p)
ax[1, 0].plot(ts, E_k+E_p)
ax[1, 0].set_ylabel("E [J]")
ax[1, 0].set_xlabel("t [s]")
ax[1, 0].legend(labels=["$E_k$", "$E_p$", "$E$"])

# Relativní chyba E
rdE = (E_0 - E_k - E_p)/E_0

ax[1, 1].set_title("Relativní chyba energie")
ax[1, 1].set_ylabel(r"$\frac{E_0 - E}{E_0}$")
ax[1, 1].set_xlabel("t [s]")
ax[1, 1].plot(ts, rdE)

plt.tight_layout()
plt.show()
