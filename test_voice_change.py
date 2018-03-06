#how to change speak speed
import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)   #change speak speed
voices = engine.getProperty('voices')
for voice in voices:
   print voice .id
   engine.setProperty('voice', voice.id)

   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()