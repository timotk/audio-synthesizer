from dataclasses import dataclass

from mido import MidiFile, tick2second
import numpy as np

sample_rate = 44100


@dataclass
class TimedNote:
    note: int
    time: float


def load_midi():
    mid = MidiFile("Melodie ding.mid")
    return mid


def get_note_timings(mid: MidiFile) -> list[TimedNote]:

    delta = 0  # Keep a running delta while looping over notes
    notes = []
    for msg in mid.tracks[1]:
        delta += msg.time
        if msg.type == 'note_on':
            sec = tick2second(delta, mid.ticks_per_beat, 468750)
            note = TimedNote(note=msg.note, time=sec)
            notes.append(note)
    return notes

def noteToFreq(note, base_frequency=880):
    return (base_frequency / 32) * (2 ** ((note - 9) / 12))


def generate_audio(notes: list[TimedNote]):
    duration = 0.2

    total_duration = max(notes, key=lambda x: x.time).time
    T = np.linspace(0, total_duration, int(total_duration * sample_rate), endpoint=False)
    A = np.zeros(len(T))
    t = np.linspace(0, duration, int(duration * sample_rate))
    for note in notes:
        frequency = noteToFreq(note.note)
        sample = np.sin(frequency * t * 2 * np.pi)
        n = len(sample)
        if note.time > 0:
            offset = int(note.time * 44100)
        else:
            offset = 0
        print(f"Putting {note.note} at {offset}")
        if len(A[0 + offset: n + offset]) < len(sample):
            continue
        A[0 + offset: n + offset] += sample

    return A


def load_notes():
    mid = load_midi()
    notes = get_note_timings(mid)
    return notes
