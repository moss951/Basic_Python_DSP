import numpy as np
import wavegen as wg

class WaveTable:
    def __init__(self, waveform_type, length_samples):
        self.waveform_type = waveform_type
        self.length_samples = length_samples
        
        self.samples = np.zeros(self.length_samples)
        self.fill_wavetable()

    def get_waveform_point(self, index):
        if self.waveform_type == 'sin':
            return wg.sine(index, self.length_samples)
        elif self.waveform_type == 'triangle':
            return wg.triangle(index, self.length_samples)
        elif self.waveform_type == 'saw':
            return wg.sawtooth(index, self.length_samples)
        elif self.waveform_type == 'square':
            return wg.square(index, self.length_samples)
            

    def fill_wavetable(self):
        for i in range(self.samples.shape[0]):
            self.samples[i] = self.get_waveform_point(i)