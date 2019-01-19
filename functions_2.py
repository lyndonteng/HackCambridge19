#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 16:30:14 2019

@author: Sehaj
"""


import abjad
import math

import numpy as np

chords = np.load('chords_test.npy')

print(chords)

notes = []
notes_inp = [0,1,2,3,4,5]
time_s = [2,1,2,1,2,2]



def plot_notes(bpm, notes_inp, time_s):
    
    number_of_measures = math.ceil(len(notes_inp)/bpm)
    
    for i in range(0,len(notes_inp)):
        
        duration = abjad.Duration(time_s[i], 4)
        notes.append(abjad.Note(notes_inp[i], duration))
        
    staff = abjad.Staff(notes)
    abjad.show(staff)
    
#plot_notes(4, notes_inp, time_s)