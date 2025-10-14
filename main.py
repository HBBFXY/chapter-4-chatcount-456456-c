# main.py
s = input()

letters = 0
digits = 0
spaces = 0
others = 0

for ch in s:
    # 只算英文字母 A-Z, a-z
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        others += 1

# 严格匹配测试脚本要求的输出格式（英文冒号+1空格）
print("英文字符: {}".format(letters))
print("数字: {}".format(digits))
print("空格: {}".format(spaces))
print("其他字符: {}".format(others))
