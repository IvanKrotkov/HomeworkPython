
def AddDictNameAndSubAndMark(dicthy,nems):
    subsAndMark = dicthy
    nameAndSubAndMark = {}
    for i in nems:
        z = {i: 0}
        nameAndSubAndMark.update(z)
    for i in nameAndSubAndMark:
        nameAndSubAndMark[i] = dict(subsAndMark.items())
    return nameAndSubAndMark
        

def AddDictSubAndMark(subs,marks):
    subAndMark = {i : marks for i in subs}
    return subAndMark
