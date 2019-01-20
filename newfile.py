# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 06:08:02 2019

@author: Admin


"""

import abjad
import math
from itertools import groupby
import numpy as np



list1 = ['C1', 'C1#', 'D1', 'D1#', 'E1', 'F1','F1#', 'G1', 'G1#', 'A1', 'B1b', 'B1', \
         'C2', 'C2#', 'D2', 'D2#', 'E2', 'F2','F2#', 'G2', 'G2#', 'A2', 'B2b', 'B2', \
         'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3','F3#', 'G3', 'G3#', 'A3', 'B3b', 'B3', \
         'C4', 'C4#', 'D4', 'D4#', 'E4', 'F4','F4#', 'G4', 'G4#', 'A4', 'B4b', 'B4', \
         'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5','F5#', 'G5', 'G5#', 'A5', 'B5b', 'B5', \
         'C6', 'C6#', 'D6', 'D6#', 'E6', 'F6','F6#', 'G6', 'G6#', 'A6', 'B6b', 'B6', \
         'C7', 'C7#', 'D7', 'D7#', 'E7', 'F7','F7#', 'G7', 'G7#', 'A7', 'B7b', 'B7',
         'C8',
         'None']
list2 = [i for i in range(-36,49,1)]
list2.append(int(100))
key_to_number = dict(zip(list1, list2))

rest_type = {'1':'r16',
             '2':'r8',
             '4':'r4'}
# the key is such since we need to divide by 16 while plotting notes

#print(list2)

#beats per minute
bpm = 92.285
one_beat_time = 60/bpm

time_sec = [1.7777777777777777, 2.6485260770975056, 2.8299319727891157, 2.9750566893424035,
            3.1564625850340136, 3.6643990929705215, 3.8095238095238093, 4.0272108843537415,
            4.244897959183674, 4.390022675736962, 4.535147392290249, 5.188208616780045, 6.095238095238095,
            7.546485260770975, 8.344671201814059, 8.671201814058957, 9.070294784580499, 9.215419501133788, 9.360544217687075, 9.687074829931973, 9.941043083900226, 10.34013605442177, 11.28344671201814, 13.206349206349206, 13.387755102040817, 13.532879818594104, 13.678004535147393, 13.82312925170068, 13.968253968253968, 14.113378684807257, 14.294784580498867, 14.439909297052154, 14.621315192743765, 14.766439909297052, 15.056689342403628, 15.310657596371883, 15.528344671201815, 15.891156462585034, 16.399092970521544, 16.58049886621315, 16.798185941043084, 17.668934240362812, 18.93877551020408, 19.26530612244898, 19.591836734693878, 19.80952380952381, 19.954648526077097, 20.244897959183675, 20.71655328798186, 21.07936507936508, 21.369614512471657, 21.768707482993197, 22.131519274376416, 25.723356009070294, 25.941043083900226, 26.086167800453516, 26.231292517006803, 26.41269841269841, 26.594104308390023, 26.73922902494331, 26.95691609977324, 27.573696145124718, 27.79138321995465, 28.408163265306122, 28.55328798185941, 28.73469387755102, 28.879818594104307, 29.06122448979592, 29.206349206349206, 29.387755102040817, 29.569160997732425, 29.714285714285715, 30.077097505668934, 30.367346938775512, 31.05668934240363, 31.201814058956916, 31.346938775510203, 31.891156462585034, 32.14512471655329, 32.326530612244895, 32.580498866213155, 32.79818594104309, 33.1609977324263, 33.342403628117914, 33.523809523809526, 33.66893424036281, 33.99546485260771, 34.72108843537415, 34.9750566893424, 35.192743764172334, 35.374149659863946, 35.66439909297052, 36.02721088435374, 36.317460317460316, 36.49886621315193, 36.68027210884354, 36.86167800453515, 37.006802721088434, 37.151927437641724, 37.333333333333336, 37.47845804988662, 37.62358276643991, 37.80498866213152, 38.02267573696145, 38.276643990929706, 38.6031746031746, 38.965986394557824, 39.147392290249435, 39.29251700680272, 39.43764172335601, 39.61904761904762, 39.80045351473923, 39.945578231292515, 40.090702947845806, 40.235827664399096, 40.4172335600907, 40.59863945578231, 40.78004535147392, 41.32426303854875, 41.57823129251701, 41.795918367346935, 41.941043083900226, 42.08616780045352, 42.26757369614513, 42.44897959183673, 42.63038548752834, 43.28344671201814, 43.718820861678005, 43.93650793650794, 44.26303854875283, 44.58956916099773, 44.91609977324263, 47.3469387755102, 47.528344671201815, 47.673469387755105, 48.0, 48.18140589569161, 48.326530612244895, 48.507936507936506, 48.6530612244898, 49.01587301587302, 49.197278911564624, 49.342403628117914, 49.487528344671205, 49.99546485260771, 50.140589569160994, 50.285714285714285, 50.61224489795919, 50.93877551020408, 51.12018140589569, 51.44671201814059, 51.6281179138322, 51.84580498866213, 51.99092970521542, 52.136054421768705, 52.317460317460316, 52.7891156462585, 52.97052154195011, 53.151927437641724, 53.4421768707483, 53.58730158730159, 53.73242630385487, 53.87755102040816, 54.276643990929706, 54.45804988662132, 54.74829931972789, 55.111111111111114, 55.32879818594105, 56.67120181405895, 57.46938775510204, 57.795918367346935, 57.941043083900226, 58.08616780045352, 58.30385487528345, 58.44897959183673, 58.59410430839002, 58.73922902494331, 58.92063492063492, 59.10204081632653, 59.28344671201814, 59.53741496598639, 59.755102040816325]
key_pressed = ['None', 'F3#', 'None', 'C4#', 'D4', 'None', 'None', 'B3', 'A3', 'None', 'D3', 
 'D3', 'D3', 'D4', 'D4', 'A3', 'D4', 'A3', 'A3', 'D4', 'E4', 'C4#', 'C4#', 'None', 'B3', 'B3', 
 'B3', 'B3', 'None', 'F3', 'C4#', 'C4#', 'D4', 'D4', 'C4#', 'C4#', 'A3', 'G3', 'None', 'None', 'None', 
 'None', 'None', 'None', 'D4', 'A3', 'A3', 'D4', 'A3', 'None', 'E4', 'C4#', 'C4#', 'None', 'F3', 'None', 
 'C4#', 'D4', 'D4', 'D4', 'C4#', 'None', 'None', 'B3', 'B3', 'C4#', 'D4', 'D4', 'C4#', 'D4', 'D4', 'D4', 
 'D3', 'None', 'A3', 'A3', 'A3', 'None', 'D4', 'A3', 'E4', 'E4', 'E4', 'C4#', 'C4#', 'C4#', 'A3', 'B3', 
 'None', 'E3', 'None', 'B3', 'B3', 'B3', 'B3', 'None', 'D4', 'C4#', 'D4', 'C4#', 'D4', 'D4', 'C4#', 'D4', 
 'None', 'D3', 'C4', 'B3', 'D3', 'D4', 'D4', 'D3#', 'D3', 'D4', 'D4', 'C4#', 'None', 'A3', 'F3#', 'A3',
 'A3', 'A3', 'None', 'D4', 'D4', 'C4#', 'E4', 'C4#', 'C4#', 'C4#', 'E3', 'None', 'None', 'F3#', 'F3#', 'F3', 'B3', 'B3', 'B3', 'B3', 'None', 'None', 'None', 'None', 'G3', 'G3#', 'G3', 'G3', 'G3', 'B3', 'B3', 'None', 'D4', 'D4', 'None', 'None', 'A3', 'A3', 'A3', 'D4', 'D4', 'D4', 'D4', 'E4', 'E4', 'None', 'C4#', 'C4#', 'C4#', 'B3', 'G3#', 'F3#', 'F3#', 'F3#', 'F3#', 'E3', 'F3#', 'B3', 'B3', 'B3', 'B3', 'None']



def convert_key_pressed_to_abjad_number(key_pressed):
    
    abjad_number =[]
    for i in range(len(key_pressed)):
        abjad_number.append(key_to_number[key_pressed[i]])
        
    return abjad_number

#print(convert_key_pressed_to_abjad_number(['C4', 'C4#']))
    

                                           
                                           
                                           
def how_many_beats(time_sec, key_pressed):
    # arg: time array in seconds 
    # want to convert to how many beats each note is, single, fourth, two?
    
    time_beat = []
    num_of_beats = []  # has number of beats of each note in fractional form
    
    key_temp = []
    
    for i in range(len(time_sec)-1):
        dur = time_sec[i+1] - time_sec[i]
        num_of_beats.append(dur/one_beat_time)
        key_temp.append(key_pressed[i])
    
    beat_lengths_frac = [0,0.25,0.5,0.75, 1, 1.5,1.75, 2,3,3.5,3.75,4]  
    
    differences = []
    num_of_beats_rounded = []
    
    for j in num_of_beats:
        x = j
        differences = [abs(x-i) for i in beat_lengths_frac]
        index = differences.index(min(differences))
        num_of_beats_rounded.append(beat_lengths_frac[index])
    
    return num_of_beats_rounded, key_temp



def draw_the_score(time_sec, key_pressed):
    
    key_as_abjad_number = convert_key_pressed_to_abjad_number(key_pressed)
    
    beats, key_temp = how_many_beats(time_sec, key_as_abjad_number)
    
    #print(beats)
    
    beats = [i*4 for i in beats]
    
    #print(beats)

    notes = []
    
    for i in range(len(beats)):
        # note: beats has been scaled up earlier by multiplying by 4!
        duration = abjad.Duration(beats[i], 16)
        if(key_as_abjad_number[i]==100):
            #notes.append(abjad.Rest('r16'))
            rest = abjad.Rest(duration)
            notes.append(rest)
        else:
            notes.append(abjad.Note(key_as_abjad_number[i], duration))
        
    staff = abjad.Staff(notes)
    abjad.show(staff)

#print(how_many_beats(time_sec, key_pressed))
    
if __name__ == '__main__':
    
    draw_the_score(time_sec, key_pressed)
        
 



"""
def time_approximation():
    return 0

def what_note(time_sec, note_played):
    #function that takes in time (in seconds) and second array with note being played
    
    for i in range(len(time_sec)-1):
        note_length = time_sec[i+1] - time_sec[1]

def plot_notes(notes_list, time_list):
    
    #number_of_measures = math.ceil(len(notes_inp)/bpm)
    
    
    notes = []
    print(time_list)
    print(len(time_list))
    print(len(notes_list))
    for i in range(len(notes_list)):
        
        duration = abjad.Duration(time_list[i], 16)
        notes.append(abjad.Note(notes_list[i], duration))
        
    staff = abjad.Staff(notes)
    abjad.show(staff)
"""
    
        
        
    