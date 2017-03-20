"""Application to Display Spectrum Analysis from .wav file"""
try:
    import wave
    import sys
    import numpy as np
    import matplotlib.pyplot as plt
    import my_filter
    import matplotlib.animation as animation
except ImportError:
    print "please install wave, sys, numpy and matplotlib"
    sys.exit(0)

# Defined Values of interest
CHUNK = 1024
RATE = 44100
TONE = 1380.0*2/RATE

# Open wave file from command line
try:
    wf = wave.open(sys.argv[1], 'rb')
except wave.Error:
    print "Could not open provided wav file or no file provided"
    sys.exit(0)

# Calculate sampling period
T=1.0/RATE

# Create a bandpass filter (Butterworth)
my_filter=my_filter.BandPass(5, TONE*0.85, TONE*1.15, RATE)

# Create plot
fig, ax = plt.subplots()

x = np.linspace(0.0, 1.0/(2.0*T), CHUNK/2)
#line, = ax.plot(x, np.sin(x))

# Seed plot with initial information
data = wf.readframes(CHUNK)
y = my_filter.filter_it(data)
line, = ax.plot(x, my_filter.get_fft(y,CHUNK))

# Define an animation function for the plot
def animate(i):
    # Get a frame
    data = wf.readframes(CHUNK)
    if data == '':
        sys.exit(0)
    # filter it
    y = my_filter.filter_it(data)
    # Update animation
    line.set_ydata(my_filter.get_fft(y,CHUNK))
    return line,


# Init only required for blitting to give a clean slate.
def init():
    # Sets up animation
    ax.set_ylim(0, 20000)
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

# Create animation
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)
# Show it
plt.show()

wf.close