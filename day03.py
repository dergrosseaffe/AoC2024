import re

pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don\'t\(\)"
total = 0
total_b = 0

content = ""
while True:

    try: s = input()
    except EOFError: break

    content += s

matches = re.findall(pattern, content)
total += sum(int(a) * int(b) for a, b in matches)

dos = re.split(do_pattern, content)
for do in dos:
    do = re.split(dont_pattern, do)[0]
    print(do)
    matches_b = re.findall(pattern, do)
    total_b += sum(int(a) * int(b) for a, b in matches_b)


print(total, total_b)