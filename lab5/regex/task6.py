import re
from dataclasses import replace


def rep(text):
    t="[., ]"
    return re.sub(t, ":", text)
text = "Hello, world. This is a test."
print (rep(text))