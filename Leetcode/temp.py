import os

hidden: true

posts = [i for i in os.listdir() if str(i).find('.md')]


for p in posts:
    print(p)
    lines = open(p, 'r', encoding='UTF-8').readlines()
    lines.insert(2, 'hidden: true\n')
    for i, l in enumerate(lines):
        if l == '  - hide\n':
            lines.pop(i)
    open(p, 'w', encoding='UTF-8').writelines(lines)