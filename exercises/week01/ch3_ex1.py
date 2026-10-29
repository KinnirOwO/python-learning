# 第3章 练习1：用字母 "P" 更新第 5 个索引；在末尾连接 "world"
s = input("请输入一个字符串：")

# 1. 字符串不可变，不能写 s[5] = "P"，只能拼一个新字符串
new_s = s[:5] + "P" + s[6:]
print("更新第5个索引后：", new_s)

# 2. 在末尾连接 "world"
result = new_s + "world"
print("末尾连接 world 后：", result)
