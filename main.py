# main.py
s = input()

letters = 0
digits = 0
spaces = 0
others = 0

for ch in s:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        others += 1

print("英文字符: {}".format(letters))
print("数字: {}".format(digits))
print("空格: {}".format(spaces))
print("其他字符: {}".format(others))
