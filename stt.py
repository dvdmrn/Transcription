from watson_developer_cloud import SpeechToTextV1
import json

stt = SpeechToTextV1()

audio_file = open("ksample2.wav","rb")

jsonobj = stt.recognize(audio_file,content_type="audio/wav")

stt.recognize

transcription = ""

for alternative in jsonobj["results"]:
    if alternative['alternatives'][0]['confidence']>0.8:
        transcription = transcription+alternative['alternatives'][0]['transcript']+"\nconfidence: "+str(alternative['alternatives'][0]['confidence'])+"\n---\n\n"
    transcription = transcription+"\n\n===\n\n"

print transcription

    #     print alternative["transcript"]+"\n"+"confidence: "+alternative["confidence"]+"\n\n"
