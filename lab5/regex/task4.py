import re
def find(text):
    t="[A-Z]{1}[a-z]+"
    matches=re.findall(t,text)
    return matches
text="Hello world This is a Test Example of Matching Pattern"
print(find(text))