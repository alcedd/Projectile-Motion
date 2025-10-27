# Projectile Motion Simulator

This project visualizes the motion of a projectile launched at an initial speed and angle using classical mechanics equations. The simulation displays both the **trajectory** of the projectile and the changes in **kinetic** and **potential** energy over time.

## 🎯 Features
- User input for initial velocity and launch angle
- Plots:
  - Projectile trajectory
  - Kinetic vs Potential energy over time
- Animated visualization using `matplotlib.animation`
- Smooth real-time motion update

## 📊 Example Visualization (Place your GIF here):

![Projectile Motion Animation](projectile_motion.gif)

> To create the GIF, uncomment the following line in the script:
```python
animation.save("projectile_motion.gif", dpi=120)
