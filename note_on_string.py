#python3
# Josh Gatka

'''
I came up with the idea for this app while reading "Vaideology" by Steve Vai.
It's essentially a flash card app but specifically for guitar.
The 'tones' list contains each note of the chromatic scale, starting with G#/Ab and ending at G natural.
The 'strings' list contains the names of each of the strings on a 6 string guitar; Low E, A, D, G, B, and High E.
The app will "draw a card", which will challenge you to play a certain tone on a specific tone.
For example, when the "G#/Ab on the low E string" card is drawn, you would put your finger on the 4th fret or the 16th fret and then strum the note.
Note that there are two places to play each tone on the guitar.
The exercise repeats until every note from each of the strings has been drawn.
Using this exercise to go through every note will result in better sightreading and improvisational skills.
Enjoy!
'''

# Task list
# TODO - create an option to choose a 7 or 8 string guitar before generating the exercises.

# Libraries
import math
import random
import os

# Variables

# Lists & Dictionaries
tones = ['G#/Ab','A','A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G'] # The full chromatic scale, including semitones
strings = ['low E string', 'A string', 'D string', 'G string', 'B string', 'high E string'] # All 6 strings
challenges = [] # will be populated with challenges like 'Play a G# on the D string.'

# functions
def create_challenges():
	for tone in tones:
		for string in strings:
			challenges.append(tone + " on the " + string)
	random.shuffle(challenges) # shuffle the exercise list
	for challenge in challenges:
		print('\n' + challenge)
		input('\nPress any key to continue...')
		os.system('clear')
	

create_challenges()
print('\nend of challenges!')
input('\nPress any key to exit...')