import re

def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)


text = "hello_world_example"
result = snake_to_camel(text)

print("CamelCase:", result)