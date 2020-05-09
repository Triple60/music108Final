import music21, librosa, os, os.path

print(len([name for name in os.listdir(r".\midi\test") if os.path.isfile(name)]))