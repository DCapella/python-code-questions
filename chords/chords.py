"""
In Western music, a major chord (major third) starts at a root note and adds
the note 4 semitones and 7 semitones above it.

A minor chord (minor third) starts at a root note and adds the note 3 semitones
and 7 semitones above it.

Given a root note root, please return an array of the major chord and the minor
chord for that root.

The notes are C, C#, D, D#, E, F, F#, G, G#, A, A#, B –– you are given this as
a constant
"""

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def chords(root):
    root_index   = notes.index(root)
    # add the 3 semitones plus 12 mod 12 to keep it in range
    middle_index = (root_index + 16) % 12
    # add the 7 semitones plus 12 mod 12  to keep it in range
    end_index    = (root_index + 19) % 12
    major = [notes[root_index], notes[middle_index], notes[end_index]]
    # minus one on the middle index to get the correct semitone for minor
    minor = [notes[root_index], notes[middle_index - 1], notes[end_index]]
    return [major, minor]
