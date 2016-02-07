#from beginning of year
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
plt.ion()

fig = plt.figure()
ax = fig.gca()
fig.suptitle("y,v vs time")
#txt = ax.text(0.0, -2.9, "")

t = np.linspace(0.0, 20.0, 499) #start val, stop val, qty
#k = [-0.1, -10.0, -17, -13]
k = [-0.01, -10.0, -17, -1]
#k[0]=coeff of damping; k[1]=gravity; k[2],k[3]=stiffness

def f_hw(y, t):
	"""For the Tacoma Narrows homework/project.
	dy/dt = v
	dv/dt = h(y)-0.1-10
	h(y) = 17y if y<0 else 13y
	
    Arguments:
    - `y`: [y, v]
    - `t`: time
    Returns: [dy/dt, dv/dt]
    """
	return [y[1], (y[0]*(k[2] if y[0]<0 else k[3])) +(k[0]*y[1]) + k[1] ]

def animate(i):
	"""Needed for the motion.  Called sequentially.
	
    Arguments:
    - `i`: for iterating
    Returns:
    """
	print(i)
	plt.cla()
	ax.set_xlabel("Time"); ax.set_ylabel("Displacement");
	#ax.text(0,0,str(i))
	plt.ylim(-3,3)
#	plt.ylim(-1000,1000)
	plt.plot(t, np_yvals[i], label=i)

#####
odeout = []
k_vals = list(range(-20, 2, 1))
for val in k_vals:
	k[0] = val/100.0
	#k[2] = val
	odeout.append(odeint(f_hw, [0,0], t))
np_yvals = np.asarray(odeout)

anim = ani.FuncAnimation(fig, animate, frames=len(k_vals), interval=100)

try:
	anim.save("out.gif",writer="imagemagick")
		  # writer=ani.MovieWriter(fps=10)) #,
except RuntimeError:
	plt.switch_backend("svg")
	anim.save("out.gif",writer="imagemagick")

print("Done")

