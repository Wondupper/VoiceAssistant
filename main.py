import stt
import DetApps
import filter
import random
import datetime
import tts
import jokes

apps = list(DetApps.give_appnames(upper=False))

def va_respond(voice: str):
    print(voice)
    cmd = filter.filter_cmd(voice,apps)
    print(cmd)
    if cmd.startswith("help") ==True:
        text = "Я умею: ..."
        text += "открывать и закрывать приложения и выводить их список ..."
        text += "рассказывать анекдоты"
        tts.va_speak(text)
        pass
    elif cmd.startswith("joke") ==True:
        tts.va_speak(random.choice(jokes.VA_JOKES))
    else:
        print()
        #DetApps.AssistandOpenOrClose(cmd)


stt.va_listen(va_respond)