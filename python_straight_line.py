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
    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_1.set_data([x[num]-200,x[num]+200],[y[num]-0.75,y[num]+0.75])

    return plane_trajectory,plane_1

fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# Subplot 1
ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))
plane_trajectory,=ax0.plot([],[],'g',linewidth=2)
plane_1,=ax0.plot([],[],'k',linewidth=10)
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)


plane_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()
