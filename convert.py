from pydub import AudioSegment

def convert_wav_to_mp3(wav_file, mp3_file):
    # Load the WAV file
    audio = AudioSegment.from_wav(wav_file)

    # Export the audio to MP3 format
    audio.export(mp3_file, format='mp3')

# Specify the input WAV file and output MP3 file paths
input_wav_file = 'input.wav'
output_mp3_file = 'output.mp3'

# Call the conversion function
convert_wav_to_mp3(input_wav_file, output_mp3_file)
