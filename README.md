# HackCambridge19
## Project Name : A-Muse
Hack Cambridge Repository

The goal of this project is to be able to create a musical staff notation for an instrument given just the audio file of a song or tune.

## Who is project for?
This project is for young aspiring musicians to encourage them to record their own tune compositions on the go and convert it to sheet music for them to use later with their instrument.

## What's next?
We would like to integrate this project as an Alexa skill, where the user plays a piece of music or hums a tune, and Alexa sends through a PDF with the corresponding staff notations. 
We are also looking to make the project compatible with all instruments. This would mean that a file with all the instruments playing would produce the required staff notations for all of them in different PDFs.

## What did we use?
We made two models to identify notes being played. One used neural networks trained to identify the notes in a music file, while the other model used fast fourier transforms to isolate the interesting frequencies and identify notes. 
Our programming language of choice was Python, and we used Flask to integrate with our html front end. 
The dependencies included librosa, adjab, and lilypond.
