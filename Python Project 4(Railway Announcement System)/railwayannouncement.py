""""
Author : Bablu Bambal
Date : 30 July 2019


required moduels
os
pandas
pydub
pyaudio
gtts
and download ffmpeg and keep it in programming files and the bin folder into the path file
"""

import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    """'
    takes the text and make a file with filename.mp3 file
    """
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang= language, slow=True)
    myobj.save(filename)



def mergeAudios(audios):
    """"
    returns the pudub audio subject
    """
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkelton():
    # generate Kripya dhayaan dijigye
    # 1- first audio file Kripya dhyaan dijigye
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")
    # 2- is form city

    # 3- se chal kar audio
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")
    # 4 -via city

    # 5 - k rashte
    start = 94000
    finish = 95200
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 --to city

    # 7 Generate ko jaane wali
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 train number and name

    # 9 generate kuch is samya mai
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 platform number

    # 11 generate per aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateAnnouncment(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate-from city
        textToSpeech(item['from'], '2_hindi.mp3')
        # 4 - Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')
        # 6 - Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')
        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")


if __name__ == '__main__':
    print("Generating Skeleton....")
    generateSkelton()
    print("Skelton Generated")
    print('good')
    generateAnnouncment("announce_hindi.xlsx")
