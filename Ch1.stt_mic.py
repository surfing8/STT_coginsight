import speech_recognition as sr

# microphone에서 auido source를 생성합니다
while True:
    i = input()
    if i == 'a':

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

# 구글 웹 음성 API로 인식하기 (하루에 제한 50회)

            print(r.recognize_google(audio, language='ko'))
        continue
    else : 
        break

