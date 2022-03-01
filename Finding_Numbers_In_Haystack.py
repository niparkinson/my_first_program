import re

hand = open('regexsum1494080.txt')

lst = list()
total = 0
for line in hand:
    number_string = re.findall("[0-9]+", line)
    if len(number_string) == 0:
        continue
    else:
        for value in number_string:
            total = total + int(value)
print(total)