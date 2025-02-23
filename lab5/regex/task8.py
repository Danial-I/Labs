import re

def split_at_uppercase(s):
    return re.findall(r'[A-Z][a-z]*', s)


text = "HelloWorldExample"
result = split_at_uppercase(text)
print("Результат:", result)
