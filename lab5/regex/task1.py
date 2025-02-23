import re
def matches(text):
    t="ab*"
    if re.fullmatch(t,text):
        return "true"
    else:
        return "false"

texts=["ab", "abb","ac","ad"]
for text in texts :
    print(text,matches(text))