import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("dark_background")

def get_float(prompt) -> float:
    while True:
        try:
            return float(input(prompt))
        except TypeError:
            print("Type error! You must enter a number.")
        except ValueError:
            print("Value error! Try again.")

class Projectile_Motion:
    def __init__(self, v, angle):
        self.v = v
        self.angle = angle

        self.calculations()
        self.creating_objects()
        self.planes_configuration()
    
    def calculations(self):
        self.V = np.array([self.v * np.cos(np.radians(self.angle)),
                           self.v * np.sin(np.radians(self.angle))]) # Velocity (m/s)
        
        self.t = np.linspace(0, (self.v * np.sin(np.radians(2 * self.angle))) / (np.cos(np.radians(self.angle)) * 9.8), 100) # Time (s)
        self.x = self.V[0] * self.t
        self.y = self.V[1] * self.t - 4.9 * (self.t ** 2)

        self.y_kinetic = (self.V[0] ** 2 + (self.V[1] - 9.8 * self.t) **2 ) / 2
        self.y_potential = 9.8 * self.y

    
    def creating_objects(self):
        self.fig, self.ax = plt.subplots(1, 2)

        """First xy-plane objects"""
        self.projectile, = self.ax[0].plot([], [],markersize="20", marker=".")
        self.ax[0].text(self.x[np.argmax(self.y)]*0.5, max(self.y) * 1.1, f"max. height {round(max(self.y), 2)} m", size=10)
        self.ax[0].text(max(self.x)/2 * 0.5, 0.05 * max(self.y), f"range {round(max(self.x), 2)} m")
        self.ax[0].plot(self.x, self.y, "b--")

        """Second xy-plane objects"""
        self.kinetic_energy, = self.ax[1].plot([], [])
        self.potential_energy, = self.ax[1].plot([], [])
    
    def planes_configuration(self):
        """First xy-plane"""
        self.ax[0].text(self.x[np.argmax(self.y)]*0.5, max(self.y) * 1.1, f"max. height {round(max(self.y), 2)} m", size=10)
        self.ax[0].text(max(self.x)/2 * 0.5, 0.05 * max(self.y), f"range {round(max(self.x), 2)} m")
        self.ax[0].plot(self.x, self.y, "b--")

        self.ax[0].set_ylim(0, max(self.y) * 1.5)
        self.ax[0].set_xlim(0, max(self.x) + 1)
        self.ax[0].set_title("Trajectory")
        self.ax[0].set_xlabel("Distance (Meters)")
        self.ax[0].set_ylabel("Distance (Meters)")
        self.ax[0].grid(alpha=0.3)

        """Second xy-plane"""
        self.ax[1].set_ylim(0, max(self.y_kinetic))
        self.ax[1].set_xlim(0, max(self.t) + 1)
        self.ax[1].legend(["Kinetic Energy", "Potential Energy"], loc="upper right")
        self.ax[1].set_title("Trajectory")
        self.ax[1].set_xlabel("Time (Seconds)")
        self.ax[1].set_ylabel("Energy (Joules)")
        self.ax[1].grid(alpha=0.3)
    
    def update_data(self, frame):
        self.projectile.set_data(self.x[(frame - 1):frame], self.y[(frame - 1):frame])
        self.kinetic_energy.set_data(self.t[:frame], self.y_kinetic[:frame])
        self.potential_energy.set_data(self.t[:frame], self.y_potential[:frame])
    
    def run(self):
        self.animation = FuncAnimation(fig=self.fig,
                           func=self.update_data,
                           frames=len(self.t),
                           interval=25, 
                           repeat=False)
        
        self.fig.tight_layout()
        # self.animation.save("projectile_motion.gif", dpi=120) Creating GIF (uncomment)

        plt.suptitle("Projectile Motion", size=20)
        plt.show()
        
v = get_float("Enter initial speed (m/s): ")
angle = get_float("Enter initial angle (degrees) < 90: ")

simulation = Projectile_Motion(v, angle)
simulation.run()