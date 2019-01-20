# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:09:20 2019

@author: Admin
"""

from abjad import *
notes = []

rest = abjad.Rest('r16')
#abjad.show(rest)

note = Note(0, Duration(16, 32))
#note.written_duration = Duration(1, 4)
notes.append(note)
notes.append(rest)


staff = abjad.Staff(notes)
abjad.show(staff)

