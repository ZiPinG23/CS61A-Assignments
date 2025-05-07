from wave import open
from struct import Struct
from math import floor

frame_rate = 11025  # 采样率 11025hz/s


def encode(x):
    i = int(16384 * x)
    return Struct('h').pack(i)


def play(sampler, name='song.wav', second=2):
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < second * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()


def tri(frequency, amplitude=0.1):
    period = frame_rate // frequency

    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave

    return sampler


c_fre, e_fre, g_fre = 261.63, 329.63, 392.00


def both(f, g):
    return lambda t: f(t) + g(t)


def note(f, start, end):
    def sampler(t):
        second = t / frame_rate
        if second < start:
            return 0
        elif second > end:
            return 0
        else:
            return f(t)

    return sampler


c, e, g = tri(c_fre), tri(e_fre), tri(g_fre)
low_g = tri(g_fre / 2)

z = 0
song = note(e, z, z + 1 / 8)
z += 1 / 8
song = both(song, note(e, z, z + 1 / 8))
z += 1 / 4
song = both(song, note(e, z, z + 1 / 8))
z += 1 / 4
song = both(song, note(c, z, z + 1 / 8))
z += 1 / 8
song = both(song, note(e, z, z + 1 / 8))
z += 1 / 4
song = both(song, note(g, z, z + 1 / 4))
z += 1 / 2
song = both(song, note(low_g, z, z + 1 / 4))
z += 1 / 2

play(song)