import numpy as np
from filter import Filter

class HighShelf(Filter):
    def __init__(self, cutoff_freq, q_db, gain_db):
        super().__init__(cutoff_freq, q_db, gain_db)

    def set_coefficients(self):
        A_add = self.A + 1
        A_sub = self.A - 1
        two_sqrtA_alpha = 2 * np.sqrt(self.A) * self.alpha_q

        self.a0 = A_add - A_sub * self.cos_w0 + two_sqrtA_alpha
        self.a1 = -2 * (A_sub - A_add * self.cos_w0)
        self.a2 = A_add - A_sub * self.cos_w0 - two_sqrtA_alpha

        self.b0 = self.A * (A_add + A_sub * self.cos_w0 + two_sqrtA_alpha)
        self.b1 = 2 * self.A * (A_sub + A_add * self.cos_w0)
        self.b2 = self.A * (A_add + A_sub * self.cos_w0 - two_sqrtA_alpha)