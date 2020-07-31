import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something:')
    r.energy_threshold = 1500
    r.pause_threshold = 0.7
    audio = r.listen(source)
    print('Done!')

text = r.recognize_google(audio, language='hi-IN')

print(text)

print(r.recognize_google(audio))
