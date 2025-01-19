pip install pyttsx3

import pyttsx3
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voice[0].id)

What Is VoiceId?

Voice id helps us to select different voices.
voice[0].id = Male voice
voice[1].id = Female voice
