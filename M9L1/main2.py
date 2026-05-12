import pyttsx3

engine = pyttsx3.init()

# Türkçe için hız
engine.setProperty("rate", 140)

# Ses seviyesi
engine.setProperty("volume", 1)

# Bilgisayardaki sesleri listele
voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(i, voice.name)

# Türkçe sese geç
# Listede Türkçe olanın numarasını yaz
engine.setProperty("voice", voices[0].id)

text = "Merhaba Ege nasılsın bugün"

engine.say(text)

engine.runAndWait()