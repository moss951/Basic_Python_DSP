import numpy as np
import biquad as bi

class Filter:
    def __init__(self, cutoff_freq, q_db, gain_db=0):
        self.cutoff_freq = cutoff_freq
        self.q_db = q_db
        self.gain_db = gain_db

        self.prev1_input = 0
        self.prev1_output = 0
        self.prev2_input = 0
        self.prev2_output = 0

        self.a0 = 0
        self.a1 = 0
        self.a2 = 0
        self.b0 = 0
        self.b1 = 0
        self.b2 = 0

        self.A = 10 ** (self.gain_db / 40)

    def process(self, input_buffer, sample_rate):
        self.set_intermediate_variables(sample_rate)
        self.set_coefficients()
        output_buffer = np.zeros(input_buffer.shape[0])

        for i in range(input_buffer.shape[0]):
            output_buffer[i] = bi.process(
                input_buffer[i], 
                self.prev1_input, self.prev1_output, self.prev2_input, self.prev2_output, 
                self.a0, self.a1, self.a2, self.b0, self.b1, self.b2
                )
            
            self.prev2_input = self.prev1_input
            self.prev1_input = input_buffer[i]

            self.prev2_output = self.prev1_output
            self.prev1_output = output_buffer[i]

        return output_buffer
    
    def set_intermediate_variables(self, sample_rate):
        self.w0 = 2 * np.pi * self.cutoff_freq / sample_rate
        self.sin_w0 = np.sin(self.w0)
        self.cos_w0 = np.cos(self.w0)
        self.alpha_q = self.sin_w0 / (2 * self.q_db)
        self.shelf_gain_db = np.power(10, self.gain_db / 40)
        self.alpha_shelf = self.sin_w0 / 2 * np.sqrt((self.shelf_gain_db + 1 / self.shelf_gain_db) * (1 / self.q_db - 1)  + 2)
    
    def set_coefficients(self):
        pass
