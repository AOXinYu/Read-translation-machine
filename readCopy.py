#-*- coding: utf-8 -*-
import  win32clipboard as wc
import  win32con
import pyttsx
import chardet
import time

def speakInit():
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    return  engine

def getCopyText():
    wc.OpenClipboard()
    try:
        copy_text= wc.GetClipboardData(win32con.CF_TEXT).replace("\r\n"," ").replace("\n"," ").replace("\r"," ")
    except:
        copy_text = "no word"
    wc.CloseClipboard()

    return  copy_text



old_text = "hi"

if __name__ == "__main__":
    old_text = "hi"
    engine = speakInit()
    while (1):

        time.sleep(1)
        print  chardet.detect(getCopyText())

        if (getCopyText() != old_text):

            try:
                engine.say(getCopyText())
                time.sleep(1)
                engine.say(getCopyText())
                engine.runAndWait()
                old_text = getCopyText()
            except:
                pass
