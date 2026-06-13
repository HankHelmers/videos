import numpy as np
import sounddevice as sd

# Creates an array of sin deminsions
def sine_tone(frequency=440, duration=1.0, sample_rate=44100):
    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False
    )

    tone = np.sin(2 * np.pi * frequency * t)

    return tone

tone1 = sine_tone(440, 1.0)
tone2 = sine_tone(880, 1.0)

# Mix the audio by summing the arrays together
mixed_audio = tone1 + tone2

# Prevent digital clipping (keep amplitude values between -1.0 and 1.0)
max_amplitude = np.max(np.abs(mixed_audio))
if max_amplitude > 1.0:
    mixed_audio /= max_amplitude

# Play the combined audio simultaneously
sd.play(tone1)
sd.wait()  # Block until playback finishes

sd.play(tone2)
sd.wait() 

sd.play(mixed_audio)
sd.wait() 
