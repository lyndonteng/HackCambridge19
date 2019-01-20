
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
         'C8']
list2 = [i for i in range(-36,49,1)]
notes_to_numbers = dict(zip(list1, list2))

#print(notes_to_numbers)


chords = np.load('chords_full.npy')
#print(chords)

sampling_rate = 0.0234

bpm = 90 # TODO: LIBROSA  

#chords = func2to1array(chords)
#print('chords')
#print(chords)






def bpm_to_bt(bpm):
    return 60/bpm
    



def func2to1array(chords_array):
    chords_array_new = []
    
    for i in range(len(chords_array)):
        chords_array_new.append(chords_array[i][0])
    return chords_array_new



    
# all good




def get_notes(chords):
    
    
    grouped_notes = [(k, sum(1 for i in g)) for k,g in groupby(chords)]
    """
    for i in grouped_notes:
        if(i[1] < 2):
            grouped_notes.remove(i)
    """
    
    
    # Or (k, len(list(g))), but that creates an intermediate list
    """
    for i in grouped_notes:
        if(i[1] < 13):
            grouped_notes.remove(i)
    """

    return grouped_notes


    """
    # rewritten
    grouped_notes = [] #list of tuples
    j=0
    
    while j < len(chords):
        temp = []
        first_ele = chords[j]
        temp.append(chords[j])
        
        if(j!=(len(chords)-1)):
               
            while chords[j+1]==chords[j]:
                temp.append(chords[j+1])
                 
                j = j+1
                if(j<len(chords)-1):
                    continue
                else:
                    break
                
        grouped_notes.append((first_ele, len(temp)))
        j = j+1
        
    """
    """        
    temp = []
    for m in range(len(chords)):
        if m==0:
            ele = chords[m]
            temp.append(ele)
        else:
            if chords[m]!=ele:
                grouped_notes.append((ele, len(temp)))
                temp = []
            else:
                temp.append(ele)
        
        
    """
 
        


def convert_back(chords):
    output_array = []
    for i in range(len(chords)):
        for j in range(int(chords[i][1])):
            output_array.append(chords[i][0])
    return output_array
    

def filter_again(chords):
    for i in chords:
        if(i[1] < 5):
            chords.remove(i)
    return chords


def time_to_beats(notes, bpm):
    # notes is array of tuple (note, freq)
    time_list = []
    for i in range(len(notes)):
        time_list.append((notes[i][1] * sampling_rate) / bpm_to_bt(bpm)) # gives total time in s per note
        
    return time_list
    
#time_to_beats()
def time_to_beats_2(time_list):
    print('waaaaaah ', len(time_list))
    beat_lengths=[0,0.25,0.5,0.75,1, 1.5,1.75, 2,3,3.5,3.75,4]
    differences = []
    beats_actual = []
    for j in time_list:
        x = j
        differences = [abs(x-i) for i in beat_lengths]
        #print(differences)
        index = differences.index(min(differences))
        beats_actual.append(beat_lengths[index]*4)
    return beats_actual

    
    
#print(time_to_tuple()) 



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
    
    
    
#plot_notes(4, notes_inp, time_s)
    
    
    
def make_notes_list(notes, time_list):
    notes_list = []
    for i in range(0, len(notes)):
        notes_list.append(notes[i][0])
    
    for i in range(0, len(notes_list)):
        notes_list[i] = notes_to_numbers[notes_list[i]]
    """
    print('################')
    print(len(notes_list))
    print(len(time_list))
    print(time_list[118])
    print(type(time_list[9]))
    print(len(time_list))
    """
    
    new_notes = []
    new_times = []
       
    """
    m=0
    while m<len(notes_list):
        #print(len(time_list))
        #print(m, ' ', time_list[m])
        if(time_list[m] != 0):
            new_notes.append(notes_list[m])
            new_times.append(time_list[m])
        m = m+1
    """
        
    #print('########')
    new_notes = notes_list
    new_times = time_list
    
    return new_notes, new_times

def remove_zeros(notes, actual_beats):   
    # and add rests!
    list1 = []
    list2 = []
        
    min_for_fourth_rest = round(641/bpm)
    
    m=0
    count = 0
    
    while m<len(notes):
        #print(len(time_list))
        #print(m, ' ', time_list[m])
        if(actual_beats[m] != 0):
        
            list1.append(notes[m])
            list2.append(actual_beats[m])
        if(actual_beats[m]==0):
            count = count+1
            if round()
            
        m = m+1
        
    #print('########')
    #print(new_notes)
    #print(new_times)
    
    return list1, list2

def add_rests(list1, list2):
    # list2 has the zeros
    count = 0
    for i in range(length(list1)):
        
        if list2[i] == 0:
            count = count+1
        if list2[i]!=0:
            





    
notes = func2to1array(chords)
#print(notes)

notes = get_notes(notes)
#print('------------------------\n\n\n-----------------')
#print(notes)
notes = convert_back(notes)
#print('------------------------\n\n\n-----------------')
#print(notes)

notes = get_notes(notes)
#print('------------------------\n\n\n-----------------')
#print(notes)



#print('\n\n\n\n\n NOTES')
#print(notes)

"""
notes = get_notes(notes)
print('\n\n\n\n\n\n\ NOTES')
print(notes)
notes = convert_back(notes)
notes = get_notes(notes)
print('\n\n\n\n\n\n\ NOTES')
print(notes)
notes = filter_again(notes)
print('\n\n\n\n\n\n\ NOTES')
print(notes)
notes = filter_again(notes)
print('\n\n\n\n\n\n\ NOTES')
print(notes)
notes = filter_again(notes)
print('\n\n\n\n\n\n\ NOTES')
print(notes)
notes = filter_again(notes)
print('\n\n\n\n\n\n\ NOTES')
print(notes)
"""


print('time list \n\n')
time_list = time_to_beats(notes, bpm)


print('note list \n\n')
#print(notes[0])
notes_list, time_list = make_notes_list(notes, time_list)

print(0 in time_list)
print(time_list)

print('Beats actual')
beats_actual = time_to_beats_2(time_list)
print('\n\n Checking length')
print(len(beats_actual))
print(len(notes_list))
print(beats_actual)

#notes, beats = remove_zeros(notes_list, beats_actual)
#print(len(beats))
#print(len(notes))
#print('\n\n printing both \n\n')
#print(notes_list, time_list)
#plot_notes(notes, beats)




# we have both lists now - note and time