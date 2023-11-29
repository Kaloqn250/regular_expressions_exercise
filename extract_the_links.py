import re

pattern = r'(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)'
links = []

line = input()

while line:
    match = re.findall(pattern, line)
    if match:
        links.append(match[0])

    line = input()

print("\n".join(links))
