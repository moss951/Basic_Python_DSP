import numpy as np

class Gain:
    def __init__(self, gain_db):
        self.gain_db = gain_db

    def process(self, input_buffer):
        gain_linear = np.power(10, self.gain_db / 10)
        output_buffer = np.zeros(input_buffer.shape[0])

        for i in range(input_buffer.shape[0]):
            output_buffer[i] = input_buffer[i] * gain_linear

        return output_buffer