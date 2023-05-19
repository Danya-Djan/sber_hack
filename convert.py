import os
from pydub import AudioSegment

def convert_wav_to_mp3(wav_file, mp3_file):
    audio = AudioSegment.from_wav(wav_file)
    audio.export(mp3_file, format='mp3')

# Specify the input folder containing WAV files
input_folder = 'train-samples/NotFraud'

# Specify the output folder to store the converted MP3 files
output_folder = 'output/NotFraud'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of WAV files in the input folder
wav_files = [f for f in os.listdir(input_folder) if f.endswith('.wav')]

# Convert each WAV file to MP3 format
for wav_file in wav_files:
    # Create the corresponding output file path
    mp3_file = os.path.join(output_folder, os.path.splitext(wav_file)[0] + '.mp3')

    # Call the conversion function
    convert_wav_to_mp3(os.path.join(input_folder, wav_file), mp3_file)
