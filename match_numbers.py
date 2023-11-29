import re

numbers = input()
pattern = r"(?:^|(?<=\s))-?\d+(?:\.\d+)?(?:$|(?=\s))"
result = re.findall(pattern, numbers)

print(' '.join(result))
