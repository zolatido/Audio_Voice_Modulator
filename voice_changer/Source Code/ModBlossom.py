#### REPORTER MODIFIED VOICE


import simpleaudio as sa
import numpy as np
import soundfile as sf

def reporter_voice_effect(input_filename, output_filename):
    # Load the input audio file
    audio_data, sample_rate = sf.read(input_filename)

    # Adjust pitch and speed
    pitch_shift_factor = 0.6  # Higher mas matinis
    speed_factor = 0.8       # Mas mataas nagiging medyo normal na yung voice bumabagal din

    # Pitch shifting and speed adjustment
    manipulated_audio = np.interp(
        np.arange(0, len(audio_data), 1.0 / speed_factor),
        np.arange(0, len(audio_data)),
        audio_data
    )

    # Calculate the new length of the manipulated audio without slicing
    new_length = int(len(manipulated_audio) / pitch_shift_factor)

    # new length
    manipulated_audio = np.interp(
        np.linspace(0, len(manipulated_audio) - 1, new_length),
        np.arange(0, len(manipulated_audio)),
        manipulated_audio
    )

    # Play the manipulated audio
    sa.play_buffer(manipulated_audio.astype(np.int16), 1, 2, sample_rate)

    # Wait until the sound has finished playing
    sa.stop_all()

    # Save the manipulated audio as a new WAV file
    sf.write(output_filename, manipulated_audio, sample_rate)

if __name__ == "__main__":
    input_filename = '03_hey_look.wav'
    output_filename = 'output_03_hey_look.wav'

    # Apply then save
    reporter_voice_effect(input_filename, output_filename)
