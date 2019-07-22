

# Solve the 1D SHE and produce a video

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from IPython import embed
from os import path


class she:
	"""
	We model the SHE (1D).
	"""
	def __init__(self, x0):
		# Initial state of the sistem.
		self.state = np.zeros(shape = N)
		self.state = x0

	def do_step(self):
		# We do one more step in the implicit Euler approximations
		self.state = np.multiply(dd, self.state + np.random.normal(loc = 0.0, scale = np.sqrt(delta_t), size = N))
		
def animate(i):
	global she_sample, ax, fig, time_text
	# Real time is:
	ani_time = i*delta_t
	# Compute the value of the solution
	value = np.dot(eigenfct_matrix, she_sample.state)
	# Redefine the plot
	lines.set_data(space, value)
	# Set the new time
	time_text.set_text("Time = {:2.3f}".format(ani_time) )
	# We print the step we are in:
	print(i)
	# And we do the next step:
	she_sample.do_step()
	return [lines,] + [time_text,]

# Number of eigenguntions
N = 1000

# Time discretisation
delta_t = 1/1000

# Diagonal for implicit Euler.
dd = 1/(1+(np.arange(1,N+1)**2)*delta_t)

# Space discretisation
space = np.arange(0.0, np.pi + 0.001, 0.001)
space_pts = len(space)
eigenfct_matrix = np.zeros(shape = (space_pts,N))

for i in range(0,N):
	eigenfct_matrix[:,i] = np.sin(i*space)*(np.sqrt(2/np.pi))

# We create a sample path
# with initial condition x0:
x0 = np.zeros(shape = (N))
she_sample = she(x0)

# We set up the picture
fig       = plt.figure()
ax        = plt.axes(xlim=(0, np.pi), ylim = (-1.5, 1.5))
time_text = ax.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes)
lines,    = ax.plot([],[], lw = 2)

# We let the animation go.
ani       = animation.FuncAnimation(fig, animate, frames=600,interval = 2, blit=True)
ani.save(filename = 'she.mp4', fps=15, extra_args=['-vcodec', 'libx264'], bitrate = -1)


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