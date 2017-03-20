"""Application to Display Spectrum Analysis from live mic"""
import pyaudio
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import my_filter

# Define samples per frame and sample rate
CHUNK = 1024
RATE = 44100

# Create and open a pyaudio strem w/ predefined parameters
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

# Sample period
T=1.0/RATE

# Create a bandpass filter (Butterworth)
my_filter = my_filter.BandPass(5,0.01,0.6,RATE)

# Create a figure
fig, ax = plt.subplots()

# define the x axis for the output of a digital filter but presented as analog
x = np.linspace(0.0, 1.0/(2.0*T), CHUNK/2)

# Read and filter initial frame to seed plot
data = stream.read(CHUNK)
output = my_filter.filter_it(data)
line, = ax.plot(x, my_filter.get_fft(output, CHUNK))

# Define an animation function to pass to animation object
def animate(i):
    """"Reads in frame of data, filters it, and projects it to the plot"""
    data = stream.read(CHUNK)
    if data == '':
        sys.exit(0)
    output = my_filter.filter_it(data)
    line.set_ydata(my_filter.get_fft(output, CHUNK))
    return line,


# Init only required for blitting to give a clean slate.
def init():
    ax.set_ylim(0, 50000)
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

# Create Animation object, passing it my own functions and figure
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=2,
                              blit=True)

# Show it
plt.show()


stream.stop_stream()
stream.close()

p.terminate()
