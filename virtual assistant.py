import speech_recognition as sr
import pyaudio
import wave
from gtts import gTTS
from playsound import playsound
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pydub import AudioSegment
from pydub.playback import play



def recognize():
    r = sr.Recognizer() #defining the speech recognizer

    wavefile = sr.AudioFile('audio.wav') #creating a file to store the audio

    with wavefile as source:
        audio = r.record(source) #storing the audio 

    text = r.recognize_google(audio) #convert the audio to text
    return text


    ### input to audio file conversion
    #guide for audio receving https://stackoverflow.com/questions/35344649/reading-input-sound-signal-using-python
    #documentation on https://people.csail.mit.edu/hubert/pyaudio/docs/

def record_wav():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16 #16 bit binary string 
    CHANNELS = 2 #number of stereo outputs
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "audio.wav"

    p = pyaudio.PyAudio() #initializes pyaudio

   

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #starts recording 

    print("say something")

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

def convert():
    try:
        record_wav()
        

    except Exception:
        pass 

    return str(recognize())

def text_to_speech(text):
    converted = gTTS(str("hellolo "+ text))
    converted.save('converted.mp3')
    sound = AudioSegment.from_mp3("converted.mp3")
    sound.export("converted.wav", format="wav")
    playsound('converted.wav')

def train():
    global chatbot
    global trainer 
    chatbot = ChatBot('Ron Obvious')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")

def converse(text):
    global chatbot
    global trainer 

    #loading pickled file 
    chatbot = ChatBot('Ron Obvious')
    response = chatbot.get_response(text)
    return response 
    
def compiled():
    while True:
        text_to_speech("say something")
        try:
            a = converse(input("input: "))
            print(a)
            text_to_speech(str(a))
        except Exception:
            pass

flag = True

while True:
    
    if flag == True:
        a = 'hi'
        print('a',str(a))
        flag = False

    if flag == False:
        b = converse(a)
        a = converse(b)
        
        print('b: ',str(b))
        print('a: ', str(a))

    
            
            
