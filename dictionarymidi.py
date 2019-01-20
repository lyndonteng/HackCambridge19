#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 05:31:24 2019

@author: ongrayyi
"""

import numpy as np

def miditonote(array):

    miditonote = {
        24 : 'C1',
        25 : 'C1#',
        26 : 'D1',
        27 : 'D1#',
        28 : 'E1',
        29 : 'F1',
        30 : 'F1#',
        31 : 'G1',
        32 : 'G1#',
        33 : 'A1',
        34 : 'B1b',
        35 : 'B1',
        36 : 'C2',
        37 : 'C2#',
        38 : 'D2',
        39 : 'D2#',
        40 : 'E2',
        41 : 'F2',
        42 : 'F2#',
        43 : 'G2',
        44 : 'G2#',
        45 : 'A2',
        46 : 'B2b',
        47 : 'B2',
        48 : 'C3',
        49 : 'C3#',
        50 : 'D3',
        51 : 'D3#',
        52 : 'E3',
        53 : 'F3',
        54 : 'F3#',
        55 : 'G3',
        56 : 'G3#',
        57 : 'A3',
        58 : 'B3b',
        59 : 'B3',
        60 : 'C4',
        61 : 'C4#',
        62 : 'D4',
        63 : 'D4#',
        64 : 'E4',
        65 : 'F4',
        66 : 'F4#',
        67 : 'G4',
        68 : 'G4#',
        69 : 'A4',
        70 : 'B4b',
        71 : 'B4',
        72 : 'C5',
        73 : 'C5#',
        74 : 'D5',
        75 : 'D5#',
        76 : 'E5',
        77 : 'F5',
        78 : 'F5#',
        79 : 'G5',
        80 : 'G5#',
        81 : 'A5',
        82 : 'B5b',
        83 : 'B5',
        84 : 'C6',
        85 : 'C6#',
        86 : 'D6',
        87 : 'D6#',
        88 : 'E6',
        89 : 'F6',
        90 : 'F6#',
        91 : 'G6',
        92 : 'G6#',
        93 : 'A6',
        94 : 'B6b',
        95 : 'B6',
        96 : 'C7',
        97 : 'C7#',
        98 : 'D7',
        99 : 'D7#',
        100 : 'E7',
        101 : 'F7',
        102 : 'F7#',
        103 : 'G7',
        104 : 'G7#',
        105 : 'A7',
        106 : 'B7b',
        107 : 'B7',
        }

    newlist = []

    for i in range(len(array)):
        if array[i] in miditonote:
            note1 = miditonote.get(array[i])
            newlist.append(note1)
        else:
            newlist.append('None')
        
        notearray = np.asarray(newlist)
        
    return notearray