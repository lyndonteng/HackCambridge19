#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:26:39 2019

@author: ongrayyi
"""

import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import peakutils
from peakutils.plot import plot as pplot

#filename = os.path.expanduser("~/Desktop/2CELLOS_-_Despacito_OFFICIAL_VIDEO-D9LrEXF3USs.wav")

def note_beats(filename):
    y, sr = librosa.load(filename)

    D = librosa.stft(y)

    D_harmonic, D_percussive = librosa.decompose.hpss(D)

    y_harmonic = librosa.istft(D_harmonic)

    hop_length = 800

    tempo, beats = librosa.beat.beat_track(y=y_harmonic, sr=sr, hop_length=hop_length)

    onset_env = librosa.onset.onset_strength(y=y_harmonic, sr=sr, aggregate=np.median, hop_length=hop_length)

    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, hop_length=hop_length)

    times = librosa.frames_to_time(np.arange(len(onset_env)), sr=sr, hop_length=hop_length)

    indexes = peakutils.peak.indexes(librosa.util.normalize(onset_env), thres=0.15, min_dist=3)
    times_peaks = []
    #values_peaks = []
    for i in indexes:
        times_peaks.append(times[i])
        #values_peaks.append(onset_env[i])
        
    return times_peaks
    

"""
plt.figure(figsize=(8, 4))
times = librosa.frames_to_time(np.arange(len(onset_env)), sr=sr, hop_length=hop_length)
plt.plot(times, librosa.util.normalize(onset_env), label='Onset strength')
plt.vlines(times[beats], 0, 1, alpha=0.5, color='r',linestyle='--', label='Beats')
plt.plot(times_peaks, librosa.util.normalize(values_peaks), 'ro')
plt.legend(frameon=True, framealpha=0.75)
# Limit the plot to a 15-second window
plt.xlim(0, 30)
plt.gca().xaxis.set_major_formatter(librosa.display.TimeFormatter())
plt.tight_layout()
"""