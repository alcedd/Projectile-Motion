import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("dark_background")

while True:
    try:
        v: float = float(input("Enter initial speed (m/s): "))
        angle: float = float(input("Enter initial angle (degrees) < 90: "))
        break
    except TypeError:
        print("Type Error! You must enter a number.")
    except ValueError:
        print("Value Error! Try again.")
        

V = np.array([v * np.cos(np.radians(angle)), v * np.sin(np.radians(angle))]) # Velocity (m/s)
t = np.linspace(0, (v * np.sin(np.radians(2 * angle))) / (np.cos(np.radians(angle)) * 9.8), 100) # Time (s)
x = V[0]*t
y = V[1]*t - 4.9*(t**2)

y_kinetic = (V[0]**2 + (V[1] - 9.8*t)**2)/2
y_potential = 9.8 * y

fig, ax = plt.subplots(1, 2)

projectile, = ax[0].plot([], [],markersize="20", marker=".")
ax[0].text(x[np.argmax(y)]*0.5, max(y) * 1.1, f"max. height {round(max(y), 2)} m", size=10)
ax[0].text(max(x)/2 * 0.5, 0.05 * max(y), f"range {round(max(x), 2)} m")
ax[0].plot(x, y, "b--")

ax[0].set_ylim(0, max(y) * 1.5)
ax[0].set_xlim(0, max(x) + 1)
ax[0].set_title("Trajectory")
ax[0].set_xlabel("Distance (Meters)")
ax[0].set_ylabel("Distance (Meters)")
ax[0].grid(alpha=0.3)

kinetic_energy, = ax[1].plot([], [])
potential_energy, = ax[1].plot([], [])

ax[1].set_ylim(0, max(y_kinetic))
ax[1].set_xlim(0, max(t) + 1)
ax[1].legend(["Kinetic Energy", "Potential Energy"], loc="upper right")
ax[1].set_title("Trajectory")
ax[1].set_xlabel("Time (Seconds)")
ax[1].set_ylabel("Energy (Joules)")
ax[1].grid(alpha=0.3)



def update_data(frame):

    projectile.set_data(x[(frame - 1):frame], y[(frame - 1):frame])
    kinetic_energy.set_data(t[:frame], y_kinetic[:frame])
    potential_energy.set_data(t[:frame], y_potential[:frame])

animation = FuncAnimation(fig=fig,
                           func=update_data,
                           frames=len(t),
                           interval=25, 
                           repeat=False)

fig.tight_layout()
# animation.save("projectile_motion.gif", dpi=120) Creating GIF (uncomment)

plt.suptitle("Projectile Motion", size=20)
plt.show()