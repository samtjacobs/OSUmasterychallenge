import scipy.signal as signal
import scipy.fftpack
import numpy as np


class BandPass(object):
    def __init__(self, order, lo, hi, RATE):
        #self.hi_d = 0.5*hi/RATE
        #self.lo_d = 0.5*lo/RATE
        self.b, self.a = signal.butter(order, [lo, hi], btype='band')
        self.zi = signal.lfilter_zi(self.b, self.a)

    def filter_it(self, data):
        data_num = np.fromstring(data, dtype=np.int16)
        y, self.zi = signal.lfilter(self.b, self.a, data_num, zi=self.zi)
        return y

    def get_fft(self, y, CHUNK):
        yf = scipy.fftpack.fft(y)
        to_return=2.0 / CHUNK * np.abs(yf[:CHUNK // 2])
        return to_return