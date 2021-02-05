# Virtual-Assistant
Download the database of the chatbot from this link and put it in the same repository as the bot  
Could't put it here because file was too big  
https://drive.google.com/file/d/1RAHOlFdUcn0kNo2GFhNOBHAhnKEB3nVQ/view?usp=sharing

## Library Requirements
pip3 install SpeechRecognition  
pip3 install PyAudio  
pip3 install Wave
pip3 install gTTS  
pip3 install playsound  
pip3 install ChatterBot
pip3 install pydub

## Conversational 
loop is written in the code to demonstrate the conversing ability of the bot [run the code to see]  
its trained on an ubuntu related conversation to help them with ubuntu interface
### Usage 
how to call the function: converse(text)  
returns: reply 

## Text to speech
### Usage
how to call the function: text_to_speech(text)

### Process of text to speech function
converts the text to speech   
saves the converted audio into mp3  
plays the mp3 audio file 

## Speech to text
start speaking when say something gets printed in the console

### Usage
how to call the function: convert()  
returns: text version of what you say
