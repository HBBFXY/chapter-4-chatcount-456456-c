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
    elif ch.isspace():
        space_count += 1
    else:
        other_count += 1

print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
