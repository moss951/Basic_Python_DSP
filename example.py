import scipy.io.wavfile as wav

from wavetable import WaveTable
from oscillator import Oscillator
from gain import Gain
from lowpass import LowPass

sample_rate = 44100
duration_secs = 5

osc = Oscillator(WaveTable('saw', 2048), 220, 180)
gain = Gain(-6)
lpf = LowPass(500, 1)

# PROCESS OUTPUT
output_buffer = osc.generate_signal(duration_secs, sample_rate)
output_buffer = gain.process(output_buffer)
output_buffer = lpf.process(output_buffer, sample_rate)

wav.write('output/output.wav', sample_rate, output_buffer)
