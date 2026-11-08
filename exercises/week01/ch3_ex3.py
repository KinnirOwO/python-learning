# 第3章 练习3：对齐、rpartition、数行数

# 1. 用字符串函数把 3 行文字对齐（宽度 20）
line1 = "Python"
line2 = "is"
line3 = "fun"
print("--- 左对齐 ljust ---")
print(line1.ljust(20, "*"))
print(line2.ljust(20, "*"))
print(line3.ljust(20, "*"))
print("--- 居中 center ---")
print(line1.center(20, "*"))
print(line2.center(20, "*"))
print(line3.center(20, "*"))
print("--- 右对齐 rjust ---")
print(line1.rjust(20, "*"))
print(line2.rjust(20, "*"))
print(line3.rjust(20, "*"))

# 2. 在分隔符"最后一次"出现的位置分成三段 → rpartition()
text = "a-b-c-d"
print(text.rpartition("-"))   # 从最后一个 - 切开
print(text.partition("-"))    # 对比：partition 从第一个 - 切开

# 3. 计算段落的行数（按题目里排版的样子分成 4 行）
paragraph = """条件编程或分支是你每天、每时每刻都在做的事情。这是关于评估条件的，如果绿灯亮，我就可
以过马路，如果下雨，我就带上雨伞，如果上班迟到，我就给经理打电话。主要工具是 if 语
句，它有不同的形式和颜色，但它基本上是计算一个表达式，并根据结果选择要执行的代码部
分。像往常一样，让我们看一个例子。"""
print("行数（count 换行符 + 1）：", paragraph.count("\n") + 1)
print("行数（splitlines）：", len(paragraph.splitlines()))
