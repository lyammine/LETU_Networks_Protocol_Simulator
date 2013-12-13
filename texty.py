# texty
# a small library of custom text formatting

# Indents a block of text by a single tab character
def tab(text):
    return "\t{0}".format(text.replace("\n", "\n\t"))

def parseSessionName(message):
    if not message.startswith("@@@RegisterRequest"):
        return False
    return message.split()[1]   # the second word is its session name

def parseNetworkParameters(message):
    word = message.split()
    return dict(through=word[4], delay=word[6], duplicate=word[8], jitterPercent=word[10], jitterMax=word[11], corruptPackets=word[13], corruptBits=word[14], timeout=word[16])
