import speech_recognition as sr
import pyaudio
import wave

'''
def recognize():
    r = sr.Recognizer() #defiing the speech recognizer

    wavefile = sr.AudioFile('audio.wav') #creating a file to store the audio
    
    with wavefile as source:
        audio = r.record(source) #storing the audio 

    print(r.recognize_ibm(audio)) #convert the audio file into text
'''


r = sr.Recognizer() #defining the speech recognizer

wavefile = sr.AudioFile('audio.wav') #creating a file to store the audio

with wavefile as source:
    audio = r.record(source) #storing the audio 

print(r.recognize_ibm(audio)) #convert the audio file into text


### input to audio file conversion
#guide for audio receving https://stackoverflow.com/questions/35344649/reading-input-sound-signal-using-python

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, #16 bit binary string 
                channels=2, #number of stereo outputs
                rate= 44100,
                input=True
                frames_per_buffer==1024)

