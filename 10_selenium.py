import time
import speech_recognition as sr
from selenium import webdriver
browser = webdriver.Chrome()

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=aa&oquery=a&tqi=U2xupdp0Jy0ssuQLQewssssssC4-056429"
browser.get(url)
browser.find_element_by_class_name("box_window").clear()
time.sleep(3)

while True:
    i = input()
    if i == 'a':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

            print(r.recognize_google(audio, language='ko'))
            browser.find_element_by_class_name("box_window").send_keys(r.recognize_google(audio, language='ko'))
            browser.find_element_by_class_name("bt_search").click()
            browser.find_element_by_class_name("box_window").clear()
        continue
    else  :
        break

