
# We simulate the Brownian sheet on [0, T] x [0, pi]


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from IPython import embed
from os import path



# Solve the KPZ equation for large times
# And two different initial conditions
# We use Space-Time discretesation (1D Finite elements)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg
from matplotlib import colors
from IPython import embed
from os import path
import sys

class fkpp:
	"""
	We model the multiplicative SHE (1D).
	"""
	def __init__(self, x_0, x_1):
		# Initial state of the first system.
		self.state_a = x_0

		# Initial state of the second system.
		self.state_b = x_1

		# We initialize the spatial noise variable.
		self.noise =  0*np.random.normal(size = (space_pts) , scale = np.sqrt(1/delta_x)) + 1
		for i in range(0,int(space_pts/4):
			self.noise[i]=-0.5

	def do_step(self):

		# We do one more step in the implicit Euler approximations
		self.state_a = np.dot(resolvent, self.state_a - (np.multiply(np.multiply( \
			self.state_a, self.state_a-1), self.noise))*delta_t )

		self.state_b = np.dot(resolvent, self.state_b - (np.multiply(np.multiply( \
			self.state_b, self.state_b-1), self.noise))*delta_t )
		#self.state = np.dot(resolvent, self.state + np.random.normal(size = (space_pts), scale = np.sqrt(delta_t/delta_x) ) ) 

def animate(i):
	# Real time is:
	ani_time = i*delta_t

	# Redefine the plot
	lines_a.set_data(space, fkpp_sample.state_a)
	lines_b.set_data(space, fkpp_sample.state_b)

	# Set the new time
	time_text.set_text("Time = {:2.3f}".format(ani_time) )
	# We print the step we are in:
	sys.stdout.flush()
	sys.stdout.write("\r Step = {}".format(i))
	# And we do the next step:
	fkpp_sample.do_step()
	return [lines_a,] + [lines_b,] + [time_text,]

# Space-Time discretisation
delta_t = 1/180
delta_x = 1/100

# Box size:
L = 10

# Space discretisation
space = np.arange(0.0, 2*np.pi*L + 0.001, delta_x)
space_pts = len(space)

# We create a sample path
# with initial condition x_0, x_1:
x_0 = np.abs(0.5*np.sin(space))
x_1 = np.abs(0.5*np.cos(space))

fkpp_sample = fkpp(x_0, x_1)

# This is the resolvent of the laplacian matrix:
# It is the laplacian with Dirichlet boundary, and we normalize
# the matrix (1-Delta) to have 1 on the diagonal.
off_value = 0.5*(1/(1+2*(delta_t/delta_x**2)) -1)
main_diag = np.ones(shape = (space_pts))
offu_diag = off_value*np.ones(shape = (space_pts-1))
to_invert = scipy.sparse.diags([offu_diag, main_diag, offu_diag], [-1, 0, 1]).toarray()

#We then invert the matrix to get the resolvent.
resolvent = scipy.linalg.inv(to_invert)/(1+2*(delta_t/delta_x**2))

#We set up the picture
fig       = plt.figure()
ax        = plt.axes(xlim=(0, 2*np.pi*L), ylim = (-0.2, 1.2))
time_text = ax.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes)
lines_a,  = ax.plot([],[], lw = 2)
lines_b,  = ax.plot([],[], lw = 2)
plt.title("FKPP Equation") 

# We let the animation go.
ani       = animation.FuncAnimation(fig, animate, frames=1200, interval = 70, blit = True)
ani.save(filename = 'fisher_kpp.mp4', extra_args=['-vcodec', 'libx264'], bitrate = 20000)


# INSTRUCTION FOR PUTTING VIDEO IN PRESENTATION.

# 1) RUN: ffmpeg -i <input> -vf scale="trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -profile:v high -pix_fmt yuv420p -g 25 -r 25 output.mp4
#	 on powershell. The result (output.mp4) is the video you will use.
# 2)  IN Latex, with package movie9 write:
#   \includemedia[
#  width=0.7\linewidth,
#  totalheight=0.7\linewidth,
#  activate=onclick,
#  %passcontext,  %show VPlayer's right-click menu
#  addresource=ballistic_out.mp4,
#  flashvars={
#    %important: same path as in `addresource'
#    source=ballistic_out.mp4
#  }
#]{\fbox{Click!}}{VPlayer.swf}