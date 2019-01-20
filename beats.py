#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:53:26 2019

@author: ongrayyi
"""

import librosa
import os

#filename = os.path.expanduser("~/Desktop/2CELLOS_-_Despacito_OFFICIAL_VIDEO-D9LrEXF3USs.wav")

def beats(filename):

    y, sr = librosa.load(filename)

    # Compute the track duration
    track_duration = librosa.get_duration(y=y, sr=sr)

    # Extract tempo and beat estimates
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # Convert beat frames to time
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    return track_duration, tempo, beat_times