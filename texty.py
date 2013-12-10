# texty
# a small library of custom text formatting

# Indents a block of text by a single tab character
def tab(text):
    return "\t{0}".format(text.replace("\n", "\n\t"))
    