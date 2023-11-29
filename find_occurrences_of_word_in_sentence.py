import re

line = input()
search_word = input()
pattern = fr'(?i)\b{search_word}\b'

matches = re.findall(pattern, line)
print(len(matches))
