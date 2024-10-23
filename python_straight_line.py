import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up the duration for your animation
t0=0 # [hrs]
t_end=2 # [hrs]
dt=0.005 # [hrs]

# Create array for time
t=np.arange(t0,t_end+dt,dt)

# Create an x array
x=800*t # [km]

# Create a y array
altitude=2 # [km]
y=np.ones(len(t))*altitude

#################### ANIMATION ####################
frame_amount=len(t)

def update_plot(num):



    return




plane_ani=animation.FuncAnimation(fig,update_plot,
        frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()
