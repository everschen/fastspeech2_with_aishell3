#!/usr/bin/python3

import sys,os
import tempfile
import librosa
import soundfile as sf
 

SAMPLE_RATE = 44100

def resample(file, path):
    target_name = os.path.basename(file)
    y, sr = librosa.load(file)
    data = librosa.resample(y, sr, SAMPLE_RATE)
    sf.write(path+ "/"+ target_name, data, SAMPLE_RATE)


srcfiles = os.listdir(sys.argv[1])

for file in srcfiles:
    print("handling the file", sys.argv[1] + file)
    resample(sys.argv[1] + file, sys.argv[2])
    print("done")
