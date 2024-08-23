from filter import Filter

class HighPass(Filter):
    def __init__(self, cutoff_freq, q_db):
        super().__init__(cutoff_freq, q_db)

    def set_coefficients(self):
        self.a0 = 1 + self.alpha_q
        self.a1 = -2 * self.cos_w0
        self.a2 = 1 - self.alpha_q

        self.b0 = (1 + self.cos_w0) / 2
        self.b1 = -(1 + self.cos_w0)
        self.b2 = self.b0