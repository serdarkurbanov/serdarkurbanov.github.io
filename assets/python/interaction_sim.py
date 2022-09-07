import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import random

#matplotlib.use('QT5Agg')

# --- classes --- # PEP8: `UpperCaseName`

class Particle:
    def __init__(self):
        self.x = 5 * np.random.random_sample()
        self.y = 5 * np.random.random_sample()
        #self.vx = 5 * np.random.random_sample() - 0.5 / 5
        #self.vy = 5 * np.random.random_sample() - 0.5 / 5
        self.vx = np.random.random_sample() / 5
        self.vy = np.random.random_sample() / 5

    def move(self):
        if self.x < 0 or self.x >= 5:
            self.vx *= -1
        if self.y < 0 or self.y >= 5:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy

# --- functions ---

def animate(frame_number):
    print('frame_number:', frame_number)

    # move all particles
    #for pi in pop:
    #    pi.move()

    # after `for`-loop

    # update data without ploting (`FunAnimation` will plot it for us)
    d.set_data([particle.x for particle in pop], [particle.y for particle in pop], ms=10000)

    # it would have to return `data` only when we use `blit=True` in `FuncAnimation`
    #return d,

# --- main ---

population = 1

pop = [Particle() for i in range(population)]

fig = plt.gcf()
ax  = plt.axes(xlim=(0, 5), ylim=(0, 5))
# draw first plot
d,  = plt.plot([particle.x for particle in pop], [particle.y for particle in pop], 'go', ms=100, dpi = 100)
anim = animation.FuncAnimation(fig, animate, frames=200, interval=45, repeat=True)#, blit=True)

plt.show()

anim.save('particles.gif', fps=25)
#anim.save('particles.gif', writer='ffmpeg', fps=25)
#anim.save('particles.gif', writer='imagemagick', fps=25)
