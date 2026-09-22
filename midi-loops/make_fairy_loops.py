"""Create three original, fairy-fountain-inspired MIDI loops and WAV previews.

No third-party Python packages are required.
"""

from array import array
import math
from pathlib import Path
import struct
import wave


PPQ = 480
EIGHTH = PPQ // 2
BAR = PPQ * 3
OUTPUT_DIR = Path(__file__).parent


def variable_length(value):
    data = [value & 0x7F]
    value >>= 7
    while value:
        data.insert(0, (value & 0x7F) | 0x80)
        value >>= 7
    return bytes(data)


def midi_track(events):
    payload = bytearray()
    previous_tick = 0
    for tick, priority, message in sorted(events, key=lambda event: (event[0], event[1])):
        payload.extend(variable_length(tick - previous_tick))
        payload.extend(message)
        previous_tick = tick
    payload.extend(b"\x00\xff\x2f\x00")
    return b"MTrk" + struct.pack(">I", len(payload)) + payload


def add_note(events, notes_for_preview, start, duration, note, velocity, channel=0):
    events.append((start, 1, bytes([0x90 | channel, note, velocity])))
    events.append((start + duration, 0, bytes([0x80 | channel, note, 0])))
    notes_for_preview.append((start, duration, note, velocity, channel))


def write_midi(filename, title, bpm, numerator, denominator_power, tracks):
    tempo = round(60_000_000 / bpm)
    title_bytes = title.encode("ascii")
    conductor = [
        (0, 0, b"\xff\x03" + bytes([len(title_bytes)]) + title_bytes),
        (0, 1, b"\xff\x51\x03" + tempo.to_bytes(3, "big")),
        (0, 2, bytes([0xFF, 0x58, 0x04, numerator, denominator_power, 24, 8])),
    ]
    chunks = [midi_track(conductor)] + [midi_track(track) for track in tracks]
    header = b"MThd" + struct.pack(">IHHH", 6, 1, len(chunks), PPQ)
    (OUTPUT_DIR / filename).write_bytes(header + b"".join(chunks))


def make_instrument_track(name, program, channel):
    encoded = name.encode("ascii")
    return [
        (0, 0, b"\xff\x03" + bytes([len(encoded)]) + encoded),
        (0, 1, bytes([0xC0 | channel, program])),
    ]


def add_arpeggios(events, preview, chords, pattern, velocity=54):
    for bar_index, chord in enumerate(chords):
        bar_start = bar_index * BAR
        for step, chord_index in enumerate(pattern):
            add_note(
                events,
                preview,
                bar_start + step * EIGHTH,
                EIGHTH - 18,
                chord[chord_index],
                velocity + (5 if step == 0 else 0),
                0,
            )


def add_melody(events, preview, bars, velocity=70):
    for bar_index, notes in enumerate(bars):
        cursor = bar_index * BAR
        for pitch, eighths in notes:
            duration = eighths * EIGHTH
            if pitch is not None:
                add_note(events, preview, cursor, duration - 24, pitch, velocity, 1)
            cursor += duration


def render_preview(filename, bpm, notes, total_ticks):
    sample_rate = 22050
    seconds_per_tick = 60.0 / bpm / PPQ
    total_seconds = total_ticks * seconds_per_tick + 0.35
    samples = array("f", [0.0]) * int(total_seconds * sample_rate)

    for start, duration, note, velocity, channel in notes:
        start_sample = int(start * seconds_per_tick * sample_rate)
        note_samples = int(duration * seconds_per_tick * sample_rate)
        frequency = 440.0 * (2.0 ** ((note - 69) / 12.0))
        gain = (velocity / 127.0) * (0.12 if channel == 0 else 0.16)
        attack = max(1, int(sample_rate * 0.012))
        release = max(1, int(sample_rate * (0.18 if channel == 0 else 0.28)))

        for index in range(note_samples):
            position = start_sample + index
            if position >= len(samples):
                break
            attack_gain = min(1.0, index / attack)
            release_gain = min(1.0, (note_samples - index) / release)
            envelope = attack_gain * release_gain * math.exp(-2.0 * index / note_samples)
            phase = 2.0 * math.pi * frequency * index / sample_rate
            if channel == 0:
                tone = math.sin(phase) + 0.28 * math.sin(2.0 * phase)
            else:
                tone = math.sin(phase) + 0.16 * math.sin(3.0 * phase)
            samples[position] += gain * envelope * tone

    peak = max(max(samples), abs(min(samples)), 0.001)
    scale = 0.86 * 32767 / peak
    pcm = array("h", (int(max(-32767, min(32767, value * scale))) for value in samples))
    with wave.open(str(OUTPUT_DIR / filename), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(pcm.tobytes())


def build_loop(filename, title, bpm, meter, chords, pattern, melody):
    harp = make_instrument_track("Harp arpeggio", 46, 0)
    bells = make_instrument_track("Bell melody", 10, 1)
    preview_notes = []
    add_arpeggios(harp, preview_notes, chords, pattern)
    add_melody(bells, preview_notes, melody)
    write_midi(filename + ".mid", title, bpm, meter[0], meter[1], [harp, bells])
    render_preview(filename + "-preview.wav", bpm, preview_notes, len(chords) * BAR)


def main():
    build_loop(
        "01-moonwell",
        "Moonwell",
        84,
        (3, 2),
        [
            [47, 54, 61, 62], [43, 50, 54, 59], [38, 45, 52, 57], [45, 52, 59, 64],
            [47, 54, 61, 62], [43, 50, 54, 59], [45, 52, 59, 64], [38, 45, 52, 57],
        ],
        [0, 1, 2, 3, 2, 1],
        [
            [(74, 2), (78, 2), (76, 2)], [(71, 2), (74, 2), (78, 2)],
            [(76, 1), (74, 1), (69, 2), (73, 2)], [(71, 2), (76, 2), (73, 2)],
            [(74, 2), (81, 2), (78, 2)], [(79, 2), (78, 1), (74, 1), (71, 2)],
            [(73, 2), (76, 2), (71, 2)], [(69, 2), (74, 4)],
        ],
    )

    build_loop(
        "02-dewdrop-dance",
        "Dewdrop Dance",
        92,
        (6, 3),
        [
            [48, 55, 59, 64], [47, 55, 62, 67], [45, 52, 59, 60], [40, 47, 50, 55],
            [41, 48, 52, 57], [40, 48, 55, 60], [38, 45, 52, 57], [43, 50, 60, 62],
        ],
        [0, 2, 1, 3, 1, 2],
        [
            [(76, 1), (79, 1), (83, 2), (79, 2)], [(74, 2), (79, 1), (81, 1), (79, 2)],
            [(72, 1), (76, 1), (79, 2), (76, 2)], [(74, 2), (71, 2), (67, 2)],
            [(69, 1), (72, 1), (76, 2), (81, 2)], [(79, 2), (76, 1), (74, 1), (72, 2)],
            [(69, 2), (74, 2), (76, 2)], [(74, 1), (72, 1), (71, 2), (67, 2)],
        ],
    )

    build_loop(
        "03-sleeping-sprite",
        "Sleeping Sprite",
        76,
        (3, 2),
        [
            [40, 47, 54, 55], [36, 43, 47, 52], [43, 50, 57, 59], [42, 50, 57, 62],
            [40, 47, 54, 55], [36, 43, 47, 52], [38, 45, 52, 57], [40, 47, 54, 59],
        ],
        [0, 1, 2, 3, 2, 1],
        [
            [(71, 2), (74, 2), (67, 2)], [(72, 2), (71, 2), (67, 2)],
            [(69, 2), (74, 2), (71, 2)], [(69, 1), (66, 1), (69, 2), (74, 2)],
            [(71, 2), (79, 2), (74, 2)], [(72, 2), (71, 1), (67, 1), (64, 2)],
            [(69, 2), (65, 2), (64, 2)], [(66, 2), (71, 4)],
        ],
    )


if __name__ == "__main__":
    main()
