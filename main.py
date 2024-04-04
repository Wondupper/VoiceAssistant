import stt
import DetApps
import filter

apps = list(DetApps.give_appnames(upper=False))

def va_respond(voice: str):
    print(voice)
    cmd = filter.filter_cmd(voice,apps)
    print(cmd)
    #DetApps.AssistandOpenOrClose(cmd)


stt.va_listen(va_respond)