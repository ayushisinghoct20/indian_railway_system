from email.mime import audio
import os
from pickle import FALSE
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS



def texToSpeach(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text = mytext, lang = language, slow = FALSE)
    myobj.save(filename)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined    

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1 - Generate kripya dheyan dijiye
    start = 88000 # in milisec
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    # 2 genrate from city
     #3 - genrate se chal kar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")

    # 4- is via-city
    #5- genrate ke  rashte
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")

    # 6 is to-city

    #7- generate ko jane wali gadi sankhiya
    start = 96000
    finish = 98000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")

    # 8 is train no and name

    # 9 -generate kuch hi shame mai platfrom sankhiya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")


    # 10 is platfrom number

    #11 - genrate par aa rhi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format="mp3")



   


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
          # 2 generate from city
          texToSpeach(item['from'],'2_hindi.mp3')

          # 4- generate via-city
          texToSpeach(item['via'],'4_hindi.mp3')

          # 6 generate to-city
          texToSpeach(item['to'],'6_hindi.mp3')

          # 8 generate train no and name
          texToSpeach(item['train_no']+" "+item['train_name'],'8_hindi.mp3')

          # 10 generate platfrom number 
          texToSpeach(item['platform'],'10_hindi.mp3')

          audio = [f"{i}_hindi.mp3" for i in range(1,12)]

          announcement = mergeAudios(audio)
          announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")
        

if __name__ == "__main__":
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
