#from beginning of year
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from mpl_toolkits.mplot3d import Axes3D
plt.ion()

fig = plt.figure()
ax  = fig.gca(projection="3d")
#axes(ylim=(-3,3)) #, xlabel="Time", ylabel="Displacement")
#ax.title("y,v vs time and k")
ax.set_xlabel("Time")
ax.set_ylabel("Displacement")
ax.set_zlabel("Damping coeff.")
plt.ylim(-3,3)
plt.show()
#txt = ax.text(0.0, -2.9, "")

t = np.linspace(0.0, 20.0, 499) #start val, stop val, qty
k = [-0.1, -10.0, -17, -13]
def z(x, y): #x is time, y pos in kvals, z is pt from odeout
	return np_yvals[k_vals.index(y)][np.where(t==x)][0];

def f_hw(y, t):
	"""For the Tacoma Narrows homework/project.
	dy/dt = v
	dv/dt = h(y)-0.1-10v
	h(y) = 17y if y<0 else 13y
	
    Arguments:
    - `y`: [y, v]
    - `t`: time
    Returns: [dy/dt, dv/dt]
    """
	return [y[1], (y[0]*(k[2] if y[0]<0 else k[3])) +(k[0]*y[1]) + k[1] ]

def animate(i):
	"""What it says on the tin"""
	print(i)
	#txt.set_text(i)
	plt.cla()
	plt.ylim(-3000,3000)
	k[2] = time_vals[i]
	for k_this in k_vals:
		k[0] = k_this/20.0
		ax.plot(t, list(zip(*odeint(f_hw, [0,0], t)))[0], k[0], "g", label=k[0])

	plt.show()
	#plt.legend(loc=1)
def main():
	ax.azim = -90 ; ax.elev = -15
	anim = ani.FuncAnimation(fig, animate, frames=len(time_vals), interval=100)
	try:
		anim.save("out.gif",writer="imagemagick")
	except RuntimeError:
		print("Fail")
		plt.switch_backend("svg")
		anim.save("out.gif",writer="imagemagick")

k_vals = list(range(-16, 4, 1)) #on the zaxis.  20xdamping coeffs
time_vals = list(range(-20, 2, 1)) #on the time axis.  Stiffness

#animate(0); input()
main()
