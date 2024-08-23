import numpy as np

class Oscillator:
    def __init__(self, wavetable, frequency, phase_deg):
        self.wavetable = wavetable
        self.frequency = frequency
        self.phase_deg = phase_deg
        self.phase_rad = phase_deg * np.pi / 180

    def generate_signal(self, duration_secs, sample_rate):
        try:
            phase_denominator = np.pi / self.phase_rad # get the phase shift relative to pi
            phase_step = self.wavetable.length_samples / 2 / phase_denominator # use phase denominator to find the corresponding start sample in wavetable
        except: # if the phase is 0
            phase_step = 0

        index = phase_step
        index_step = self.wavetable.length_samples * self.frequency / sample_rate

        output_buffer = np.zeros(duration_secs * sample_rate)

        for i in range(output_buffer.shape[0]):
            output_buffer[i] = self.interpolate_wavetable_index(index)

            index += index_step
            index %= self.wavetable.length_samples

        return output_buffer

    def interpolate_wavetable_index(self, index):
        prev_index = int(np.floor(index))
        next_index = (prev_index + 1) % self.wavetable.length_samples

        next_index_weight = index - prev_index
        prev_index_weight = 1 - next_index_weight

        return prev_index_weight * self.wavetable.samples[prev_index] + next_index_weight * self.wavetable.samples[next_index]
    