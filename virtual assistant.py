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
#documentation on https://people.csail.mit.edu/hubert/pyaudio/docs/


def record_wav():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16 #16 bit binary string 
    CHANNELS = 2 #number of stereo outputs
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio() #initializes pyaudio 

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #starts recording 

    frames = []

###### still to be changed 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream() #stop 
    stream.close()
    p.terminate()
######

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb') #creates and store into a wave file
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()