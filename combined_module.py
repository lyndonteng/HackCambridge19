import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import peakutils
import vamp
import matplotlib.pyplot as plt
import audiolazy
from peakutils.plot import plot as pplot
from IPython import get_ipython
from scorecreator import draw_the_score
#takes an audio file, outputs an array of trigger times.
def note_beats(filename):
    print('loading audio file...\n')
    y, sr = librosa.load(filename)
    
    print('putting file through fourier transform to separate harmonic and percussive\n')
    D = librosa.stft(y)
    
    print('getting melody rhythm...\n')
    D_harmonic, D_percussive = librosa.decompose.hpss(D)

    y_harmonic = librosa.istft(D_harmonic)

    hop_length = 800

    tempo, beats = librosa.beat.beat_track(y=y_harmonic, sr=sr, hop_length=hop_length)

    onset_env = librosa.onset.onset_strength(y=y_harmonic, sr=sr, aggregate=np.median, hop_length=hop_length)

    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, hop_length=hop_length)

    times = librosa.frames_to_time(np.arange(len(onset_env)), sr=sr, hop_length=hop_length)

    indexes = peakutils.peak.indexes(librosa.util.normalize(onset_env), thres=0.1, min_dist=3)
    times_peaks = []
    for i in indexes:
        times_peaks.append(times[i])
        
    print('melody rhythm generated!\n')
    return times_peaks

def get_beats(filename):
    y, sr = librosa.load(filename)
    # Compute the track duration
    track_duration = librosa.get_duration(y=y, sr=sr)
    # Extract tempo and beat estimates
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return track_duration, tempo


#converts array of midi values to array of chords
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

#converts audio file to array of midi values
def get_melody(filename):
    
    # This is how we load audio using Librosa
    print('loading audio...\n')
    audio, sr = librosa.load(filename, sr=44100, mono=True)
    print('getting melody line...\n')
    data = vamp.collect(audio, sr, "mtg-melodia:melodia")
    hop, melody = data['vector']
    timestamps = 8 * 128/44100.0 + np.arange(len(melody)) * (128/44100.0)
    
    # A clearer option is to get rid of the negative values before plotting
    melody_pos = melody[:]
    melody_pos[melody<=0] = None
    
    print('converting melody line to midi...\n)
    midi = 69 + 12*np.log2(melody_pos/440.)
    midi = np.round(midi)
    midi.astype(int)
    #np.savetxt(str(name)+".csv", midi, delimiter = ",")
    return midi

#switch identifies the switch in notes being played.
#takes array of chords as input and a filepath for beat time to consume
#outputs an array of chords corresponding to the trigger times on beat_time
def switch(chords, filepath):
    time_list = []
    note_list = []
    for i in note_beats(filepath):
        j = int(i/0.0029) + 15
        time_list.append(i)
        note_list.append(chords[j])
    return time_list, note_list

#runs module
if __name__== "__main__":
    #"/Users/ongrayyi/Documents/GitHub/HackCambridge19/FlaskWebProject2/static/data/2CELLOS_-_Despacito_OFFICIAL_VIDEO-D9LrEXF3USs.wav"
    test= "/Users/ongrayyi/Documents/GitHub/HackCambridge19/FlaskWebProject2/static/data/2CELLOS_-_Despacito_OFFICIAL_VIDEO-D9LrEXF3USs.wav"
    filename = os.path.expanduser(test)
    midi = get_melody(filename)
    chords = miditonote(midi)
    print('generating score...\n')
    draw_the_score(switch(chords, filename)[0], switch(chords, filename)[1], get_beats(filename)[1])

    
