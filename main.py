# main.py
s = input()

letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

for ch in s:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letter_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == ' ':
        space_count += 1
    else:
        other_count += 1

print("英文字符: {}".format(letter_count))
print("数字: {}".format(digit_count))
print("空格: {}".format(space_count))
print("其他字符: {}".format(other_count))
