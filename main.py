# main.py
s = input()

# 统计变量
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

for ch in s:
    # 判断英文字母（仅 A-Z/a-z）
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letter_count += 1
    # 判断数字
    elif ch.isdigit():
        digit_count += 1
    # 判断空格
    elif ch.isspace():
        space_count += 1
    # 其他字符（包括中文、符号等）
    else:
        other_count += 1

# 输出格式必须完全一致
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")

