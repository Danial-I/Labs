import re
def find (text ):
    t="a.b"
    if re.fullmatch(t,text):
        return "true"
    else :
        return "false"

text =["ab", "axb", "a123b", "acb", "babab", "abc", "a_b"]
for t in text:
    print(t,find(t))