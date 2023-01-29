import input_date as id

def AddDictNameAndSubAndMark(dicthy,nems):
    subsAndMark = dicthy
    nameAndSubAndMark = {}
    for i in nems:
        z = {i: 0}
        nameAndSubAndMark.update(z)
    for i in nameAndSubAndMark:
        nameAndSubAndMark[i] = dict(subsAndMark.items())
    return nameAndSubAndMark
        
def AddDictSubAndMark(subs):
    subAndMark = {i : id.InitMark() for i in subs}
    return subAndMark


def AddDictSubAndMarkRandom(subs):
    subAndMark = {i : id.RandomMarks() for i in subs}
    return subAndMark

