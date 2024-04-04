from strsimpy.damerau import Damerau

def filter_cmd(cmd: str,apps):
    cmd = cmd.strip()
    words = cmd.split()
    if len(words)>=2:
        firstPart = filter_firstPart(words[0])
        secondPart = filter_secondPart(' '.join(words[1:]),apps)
        return ' '.join([firstPart,secondPart])
    elif len(words)==1:
        firstPart = filter_firstPart(words[0])
        return firstPart
    else:
        return cmd

def filter_firstPart(firstPart:str):
    comands = ["open","close","list"]
    metrix= Damerau()
    setter = dict()
    for el in comands:
        setter[el] = metrix.distance(el,firstPart)
    setter2 = dict(sorted(setter.items(), key=lambda item: item[1]))
    result = list(setter2.keys())[0]
    return result

    
def filter_secondPart(secondPart:str,apps:list):
    metrix = Damerau()
    setter = dict()
    for el in apps:
        setter[el] = metrix.distance(el,secondPart)
    maxim = max(setter.values())
    minim = min(setter.values())
    for el in setter:
        setter[el] = (setter[el]-minim)/(maxim-minim)
    setter2 = dict(sorted(setter.items(), key=lambda item: item[1]))
    return list(setter2.keys())[0]

