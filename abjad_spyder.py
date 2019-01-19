# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:09:20 2019

@author: Admin
"""

from abjad import *


note = Note('r8')
note.written_duration = Duration(1, 4)
show(note)
