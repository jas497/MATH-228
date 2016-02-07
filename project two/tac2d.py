import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
plt.ion()

fig = plt.figure()
t = np.linspace(0.0, 20.0, 499) #start val, stop val, qty
#k = [-0.1, -10.0, -17, -13]
k = [-0.01, -10.0, -17, -1]
init = [0,0]
#k[0]=coeff of damping; k[1]=gravity; k[2],k[3]=stiffness

def f_hw(y, t):
	"""For the Tacoma Narrows homework/project.
	dy/dt = v
	dv/dt = h(y)-0.1v-10
	h(y) = 17y if y<0 else 13y
	
    Arguments:
    - `y`: [y, v]
    - `t`: time
    Returns: [dy/dt, dv/dt]
    """
	return [y[1], (y[0]*(k[2] if y[0]<0 else k[3])) +(k[0]*y[1]) + k[1] ]

plt.cla()
plt.xlabel("Time");
plt.ylabel("Displacement");
#plt.title("Assorted initial conditions")
#plt.title("Negative stiffness values");
plt.title("Varying alpha in Lazer-McKenna")
#plt.ylim(-1,0)
#####
#k_vals = [(-17,-13), (-14, -10), (-11, -7)]
k_vals = [-0.1, -0.5, -1.0, -2.0]
#k_vals = list(range(-5, 6, 1))
for val in k_vals:
	k[0] = val/10.0 #thus, damping is 0.01
	#k[2] = val[0]; k[3] = val[1]
	#init[1] = val/10.0 #change start pos., leave velocity alone
	plt.plot(t, list(zip(*odeint(f_hw, init, t)))[0], 
			 label="Alpha="+str(-1*k[0]) )
			 #label="Began at y,v="+str(init))

plt.legend(loc="upper right")
plt.savefig("out.png")

print("Done")
