
import os
import sys

lst = [i for i in os.listdir() if str(i).find('.md') != -1]

for name in lst:
    print(name)
    lines = open(name, 'r', encoding='UTF-8').readlines()
    for i, n in enumerate(lines):
        print(str(n))
        if str(n) == 'tags:\n':
            lines.insert(i+1, '  - hide\n')
            break
    open(name, 'w', encoding='UTF-8').writelines(lines)