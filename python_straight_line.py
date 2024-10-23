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
    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])

    return plane_trajectory,plane_1,plane_2

fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# Subplot 1
ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))
plane_trajectory,=ax0.plot([],[],'g',linewidth=2)
plane_1,=ax0.plot([],[],'k',linewidth=10)
plane_2,=ax0.plot([],[],'k',linewidth=5)

# Draw buildings
building_1,=ax0.plot([100,100],[0,1.0],'k',linewidth=7)
building_2,=ax0.plot([300,300],[0,1.0],'k',linewidth=7)
building_3,=ax0.plot([700,700],[0,0.7],'k',linewidth=15)
building_4,=ax0.plot([900,900],[0,0.9],'k',linewidth=10)
building_5,=ax0.plot([1300,1300],[0,1.0],'k',linewidth=20)
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)


plane_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()
