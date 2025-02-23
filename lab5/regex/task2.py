import re
def matches(text):
    t="ab{2,3}"
    if re.fullmatch(t,text):
        return "true"
    else :
        return "false"
texts=["ab","abb","abbb","abbbb","acbb"]
for text  in texts:
    print(text,matches(text))