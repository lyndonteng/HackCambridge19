# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:09:20 2019

@author: Admin
"""

import abjad
duration = abjad.Duration(1, 4)
notes = [abjad.Note(pitch, duration) for pitch in [0,3,5,2,1,6]]
staff = abjad.Staff(notes)
abjad.show(staff)