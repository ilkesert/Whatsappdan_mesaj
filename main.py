import webbrowser
import time
import pyautogui

kisi = input(str("Kişinin numarasını giriniz"))
mesaj = input("Yazmak istediğiniz mesajı giriniz")
webbrowser.open('https://web.whatsapp.com/send?phone=' + kisi + '&text=' + mesaj)
time.sleep(30)
pyautogui.press('enter')
print("gönderildi")
#Eğer istenilirse ses alma modülü kurulup onunla beraber yazı yazmadan sesli halde kurulabilir. Yardım için iletişime geçebilirsiniz.