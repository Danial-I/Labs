import re
def find(text):
    t="[a-z]+_[a-z]+"
    matches = re.findall(t, text)
    return matches

text="hello_world test Example_of_text another_test"
print(find(text))
